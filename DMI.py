import numpy as np
import threading
import time


def dmi_task(num_agents, num_choices, num_questions, list_answers, repeated_times, i, j, list_scores_i):
    for t in range(repeated_times):
        mat1 = np.zeros((num_choices,num_choices))
        mat2 = np.zeros((num_choices,num_choices))
        chosen = np.random.choice(range(num_questions), size=int(num_questions / 2))
        judge = np.zeros(num_questions)
        for k in chosen:
            judge[k] = 1
        for q in range(num_questions):
            if judge[q]:
                mat1[list_answers[i][q]][list_answers[j][q]] += 1
            else:
                mat2[list_answers[i][q]][list_answers[j][q]] += 1
        list_scores_i += np.linalg.det(mat1) * np.linalg.det(mat2)
    
    # debug
    # print(mat1)
    # print(mat2)
    print("Agent i {}/{}, Agent j {}/{} finished.".format(
            i, num_agents,
            j, num_agents,
            ))




# num_choices: the number of choices in each question.
# num_questions: the number of questions.
# num_agents: the number of agents attending the test.
# repeated_times: the number of repeated times of calculating DMI scores.
# list_answers: the list of agents' answers.
# list_answers[i][j]=k \in [0, num_choices) means agent i choose k in the j-th question
# list_scores: return the list of DMI scores.
def calculate_dmi(num_choices, num_questions, num_agents, repeated_times, list_answers, multi_thread=False):
    if num_choices < 1 or num_questions < 1 or num_agents < 1 or repeated_times < 1:
        print("Invalid input: negative elements!")
        return None
    if num_choices * 2 > num_questions:
        print("Invalid input for DMI calculation: the number of questions is too small!")
        return None
    for i in range(num_agents):
        for j in range(num_questions):
            if list_answers[i][j] < 0 or list_answers[i][j] >= num_choices:
                print("Invalid input for DMI calculation: invalid element in list_answers!")
                return None
    list_scores = np.zeros(num_agents)
    # debug
    # print(list_answers)
    if multi_thread:
        print("Multi threading.")
        # multithread version
        for i in range(num_agents):
            threads = []
            start_time = time.time()
            for j in range(num_agents):
                if i == j:
                    continue
                task_thread = threading.Thread(target=dmi_task, 
                    args=(num_agents, num_choices, num_questions, list_answers, repeated_times, i, j, list_scores[i]))
                threads.append(task_thread)
                task_thread.start()
            for task_thread in threads:
                task_thread.join()
            print("Agent i {}/{} cost time {}.".format(
                    i, num_agents,
                    time.time()-start_time
                    ))
    else:
        # non-multi-thread version
        start_time = time.time()
        for i in range(num_agents):
            for j in range(num_agents):
                if i == j:
                    continue
                for t in range(repeated_times):
                    mat1 = np.zeros((num_choices,num_choices))
                    mat2 = np.zeros((num_choices,num_choices))
                    chosen = np.random.choice(range(num_questions), size=int(num_questions / 2))
                    judge = np.zeros(num_questions)
                    for k in chosen:
                        judge[k] = 1
                    for q in range(num_questions):
                        if judge[q]:
                            mat1[list_answers[i][q]][list_answers[j][q]] += 1
                        else:
                            mat2[list_answers[i][q]][list_answers[j][q]] += 1
                    list_scores[i] += np.linalg.det(mat1) * np.linalg.det(mat2)
                print("Agent i {}/{}, Agent j {}/{} finished.\r".format(
                        i, num_agents,
                        j, num_agents,
                        ), end="")
            print("Agent i {}/{} cost time {}.".format(
                    i, num_agents,
                    time.time()-start_time
                    ))

    list_scores = list_scores / repeated_times
    print("\n")
    return list_scores