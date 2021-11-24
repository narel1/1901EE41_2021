# import regex and pandas
import pandas as pd
import re


def get_lecture_tut_practical(string_ltp):
    # split the string by '-' to get an LTP_list of strings
    LTP_list = string_ltp.split('-')
    return LTP_list


def check_roll_number(roll_num):
    # check whether the entry is roll number or not
    return re.match(r"\d\d\d\d\w\w\d\d", roll_num)


def get_full_list(subject_registered):
    result_list = set()
    for index, levels in subject_registered.iterrows():
        subject = levels["subno"]
        if check_roll_number(levels["rollno"]):
            if subject not in subject_lecture_tut_practical:
                print("subject not included")
            if subject_lecture_tut_practical[subject][0] != "0":
                result_list.add((levels["rollno"], levels["subno"], "1"))
            if subject_lecture_tut_practical[subject][1] != "0":
                result_list.add((levels["rollno"], levels["subno"], "2"))
            if subject_lecture_tut_practical[subject][2] != "0":
                result_list.add((levels["rollno"], levels["subno"], "3"))

    return result_list


def get_done_list(collect_feedback):
    result_list = set()
    for index, levels in collect_feedback.iterrows():
        if check_roll_number(levels["stud_roll"]):
            result_list.add(
                (levels["stud_roll"], levels["course_code"], str(levels["feedback_type"])))
    return result_list


# opening the required files
collect_feedback = pd.read_csv("course_feedback_submitted_by_students.csv")
course_master = pd.read_csv("course_master_dont_open_in_excel.csv")
collect_student_info = pd.read_csv("studentinfo.csv")
subject_registered = pd.read_csv("course_registered_by_all_students.csv")

# creating a dataframe with given columns needed in pandas
feedback_remaining_file = pd.DataFrame(columns=["Roll Number", "Registered Sem",
                                                "Scheduled Sem", "Course Code", "Name", "Email", "AEmail", "Contact"])

# create an empty dictionary semester_scheduled
semester_scheduled = {}

for index, levels in subject_registered.iterrows():

    # finding out if it matching the pattern "\d\d\d\d\w\w\d\d"
    if check_roll_number(levels["rollno"]):

        # put the value as empty dictionary for the key( rollno ) which
        # is already not present in the dictionary
        if levels["rollno"] not in semester_scheduled:
            semester_scheduled[levels["rollno"]] = {}

        # put the key as subno and value as tuple of register_sem and  schedule_sem
        semester_scheduled[levels["rollno"]][levels["subno"]] = (
            levels["register_sem"], levels["schedule_sem"])


# create an empty dictionary subject_lecture_tut_practical
subject_lecture_tut_practical = {}

# get LTP values for every subject by function get_lecture_tut_practical(levels["ltp"])
for index, levels in course_master.iterrows():
    subject_lecture_tut_practical[levels["subno"]
                                  ] = get_lecture_tut_practical(levels["ltp"])


full_list = get_full_list(subject_registered)

info_collector = {}

for index, levels in collect_student_info.iterrows():
    info_collector[levels["Roll No"]] = {}
    info_collector[levels["Roll No"]] = levels

done_list = get_done_list(collect_feedback)
# done_list.sort()

full_list = full_list | done_list
temp_list = done_list ^ full_list


for level in temp_list:
    # print(entry)
    roll_num = level[0]
    subject = level[1]
    feed_type = level[2]
    reg_sem = semester_scheduled[roll_num][subject][0]
    sched_sem = semester_scheduled[roll_num][subject][1]
    if roll_num in info_collector:
        name = info_collector[roll_num]["Name"]
        mail = info_collector[roll_num]["email"]
        alternate_email = info_collector[roll_num]["aemail"]
        contact = info_collector[roll_num]["contact"]
        new_fb_not_given = {"Roll Number": roll_num, "Registered Sem": reg_sem, "Scheduled Sem": sched_sem,
                            "Course Code": subject, "Email": mail, "AEmail": alternate_email, "Contact": contact, "Name": name}
        # print(new_fb_not_given)
        feedback_remaining_file = feedback_remaining_file.append(
            new_fb_not_given, ignore_index=True)

# export the DataFrame to the excel file.
feedback_remaining_file.to_excel("course_feedback_remaining.xlsx", index=False)