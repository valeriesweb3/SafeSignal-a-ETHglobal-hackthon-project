import numpy as np
import copy


# Linearly engage the choices according to scores (ignore negative ones)
# num_questions: number of questions
# num_agents: number of agents
# choices: the set of choices from agents
# choices[j][i] means agents j select choice choices[j][i] on question i
# scores: the scores of agents
# return a set of results
def aggregator_linear(num_questions, num_agents, choices, scores):
    results = np.zeros(num_questions)
    for i in range(num_questions):
        total_rights = 0
        total_sum = 0
        for j in range(num_agents):
            if scores[j] > 0:
                total_rights += scores[j]
                total_sum += scores[j] * choices[j][i]
        results[i] = total_sum / total_rights
    return results


# Transforming scores into log(1+x) (ignore negative ones).
# Linearly engage the choices according to new scores.
# num_questions: number of questions
# num_agents: number of agents
# choices: the set of choices from agents
# choices[j][i] means agents j select choice choices[j][i] on question i
# scores: the scores of agents
# return a set of results
def aggregator_log(num_questions, num_agents, choices, scores):
    log_scores = copy.deepcopy(scores)
    for j in range(num_agents):
        if log_scores[j] < 0:
            log_scores[j] = 0
    log_scores = np.log(log_scores + 1)
    results = np.zeros(num_questions)
    for i in range(num_questions):
        total_rights = 0
        total_sum = 0
        for j in range(num_agents):
            if scores[j] > 0:
                total_rights += log_scores[j]
                total_sum += log_scores[j] * choices[j][i]
        results[i] = total_sum / total_rights
    return results


# Transforming scores into tanh(x) (ignore negative ones).
# Linearly engage the choices according to new scores.
# num_questions: number of questions
# num_agents: number of agents
# choices: the set of choices from agents
# choices[j][i] means agents j select choice choices[j][i] on question i
# scores: the scores of agents
# normalization: adjust the total weight of positive scores.
# normalization = 0 means there is no normalization.
# return a set of results
def aggregator_tanh(num_questions, num_agents, choices, scores, normalization=0):
    tanh_scores = copy.deepcopy(scores)
    if normalization:
        total_rights = 0.0
        for j in range(num_agents):
            if tanh_scores[j] > 0:
                total_rights += tanh_scores[j]
        tanh_scores = tanh_scores * normalization / total_rights
    tanh_scores = np.tanh(tanh_scores)
    results = np.zeros(num_questions)
    for i in range(num_questions):
        total_rights = 0
        total_sum = 0
        for j in range(num_agents):
            if scores[j] > 0:
                total_rights += tanh_scores[j]
                total_sum += tanh_scores[j] * choices[j][i]
        results[i] = total_sum / total_rights
    return results


# Adopt the result with maximal score
# num_questions: number of questions
# num_agents: number of agents
# choices: the set of choices from agents
# choices[j][i] means agents j select choice choices[j][i] on question i
# scores: the scores of agents
# return a set of results
def aggregator_max(num_questions, num_agents, choices, scores):
    max_rights = 0
    max_agents = -1
    for j in range(num_agents):
        if scores[j] > max_rights:
            max_agents = j
    results = copy.deepcopy(choices[max_agents])
    return results


# Return the mean of choices from agents with n maximal scores
# num_questions: number of questions
# num_agents: number of agents
# choices: the set of choices from agents
# choices[j][i] means agents j select choice choices[j][i] on question i
# scores: the scores of agents
# n: n agents with maxinal scores
# return a set of results
def aggregator_maxn(num_questions, num_agents, choices, scores, n):
    indexes = np.argsort(scores, axis=-1, kind='quicksort', order=None)
    maxn_index = np.zeros(n, dtype=int)
    for k in range(n):
        maxn_index[k] = indexes[num_agents-1-k]
    results = np.zeros(num_questions)
    print(maxn_index)
    for k in range(n):
        results += choices[maxn_index[k]]
    results /= n
    return results
