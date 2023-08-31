class Job:
    def __init__(self, taskid, deadline, profit):
        self.taskid, self.deadline, self.profit = taskid, deadline, profit


def schedule_jobs(jobs, T):
    profit, slot = 0, [0] * T
    jobs.sort(key=lambda x: x.profit, reverse=True)

    for jobs in jobs:
        for i in range(min(jobs.deadline - 1, T - 1), -1, -1):
            if not slot[i]:
                slot[i] = jobs.taskid
                profit += jobs.profit
                break

    print("Scheduled Jobs:", [x for x in slot if x])
    print("Total Profit:", profit)


jobs = [
    Job(int(input(f"Task ID for Job {i + 1}: ")),
        int(input(f"Deadline for Job {i + 1}: ")),
        int(input(f"Profit for Job {i + 1}: ")))
    for i in range(int(input("Enter number of jobs: ")))]
T = int(input("Enter Deadline Limit: "))
schedule_jobs(jobs, T)