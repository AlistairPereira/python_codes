# me and co-worker
# acess to my calendar and co-workers calendar
# (which conatin meetings of both me and my co-workers for the day)
# in starttime and endtime
#also working hrs of both
#earlieststarttime and latestendtime :- daily working hrs
# meeting duration : 30 mins
#output [11:30-12:00],[15:00-15:30],[18:00-18:30]
your_calendar= [['9:00','10:30'],['12:00','13:00'],['16:00','18:00']]
ywh= ['9:00','20:00']
your_coworkers_calender=[['10:00','11:30'],['12:30','14:30'],['14:30','15:00'],['16:00','17:00']]
ycwh=['10:00','18:30']
md =30
your_start_time='9:00'
coworker_ending_time='18:30'


from datetime import datetime

#function to convert time from 'HH:MM' to hours
def convert_to_float_time(time_str):
    time_obj = datetime.strptime(time_str, '%H:%M')
    return time_obj.hour + time_obj.minute / 60.0

#convert float time back to 'HH:MM'
def convert_to_time_string(time_float):
    hours = int(time_float)
    minutes = int((time_float - hours) * 60)
    return f'{hours:02}:{minutes:02}'

def find_free_slots(your_calendar, your_coworkers_calendar, your_start_time, coworker_ending_time):
    your_calendar = [[convert_to_float_time(start), convert_to_float_time(end)] for start, end in your_calendar]
    your_coworkers_calendar = [[convert_to_float_time(start), convert_to_float_time(end)] for start, end in your_coworkers_calendar]
    
    your_start_time = convert_to_float_time(your_start_time)
    coworker_ending_time = convert_to_float_time(coworker_ending_time)
    
    all_intervals = your_calendar + your_coworkers_calendar     #combining both calendars in one list & sorting by start time
    all_intervals.sort(key=lambda interval: interval[0])
    
    merged_intervals = []
    for interval in all_intervals:
        if len(merged_intervals) == 0: #if no merged intervals are there,then add the first time slot
            merged_intervals.append(interval)
        else:
            last_interval = merged_intervals[-1]
            if last_interval[1] < interval[0]:
                merged_intervals.append(interval)
            else:
                last_interval[1] = max(last_interval[1], interval[1])
    
    free_slots = []
    end_of_last_interval = your_start_time  # 9:00 as start time
    for start, end in merged_intervals:
        if start > end_of_last_interval:
            free_slots.append([end_of_last_interval, start])
        end_of_last_interval = end
    
    if end_of_last_interval < coworker_ending_time: # 18:30 as end time
        free_slots.append([end_of_last_interval, coworker_ending_time])
    
    free_slots = [[convert_to_time_string(start), convert_to_time_string(end)] for start, end in free_slots]
    
    return free_slots

free_slots = find_free_slots([['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']],
                             [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']],
                             '9:00',
                             '18:30')
print(free_slots)

# Worst Case Time Complexitiy :  O((n + m) log (n + m)) 
#n is my first list- your_calender
#m is my second list - your_coworkers_calender
# sorting takes more time as the list grows so it takes  log(n+m)
# combining first_list , second_list and sorting gets O((n + m) log (n + m)) 

# Worst Case Space Complexity : O(n+m)
# storing a list of size n (your_calend) and list of size m (your_coworkers_calender) will give me space complexity of O(n+m).

print("----------------------------------------")


#x=[[2,1,2],[3,2,3],[2,2,8],[2,3,4],[1,3,1],[4,4,5]]

# def stacks(x):
#     sort_x = sorted(x, reverse=True)
#     print(f"sort_x: {sort_x}")
#     valid_disks=[]
#     for index,value in enumerate(sort_x):
#         width_current=value
#         depth_current=value
#         height_current=value
        
#         #comparing the current stack with the next stacks
#         meets_criteria=False
#         for next_stack in sort_x[index+1:]:
#             width_next_stack= next_stack
#             depth_next_stack= next_stack
#             height_next_stack= next_stack
        
#             x=f"Comparing {value} with {next_stack}"
#             #print(value)
#             #print(next_stack)
#             print(x)
            
            
#             if (width_current > width_next_stack and
#                 depth_current > depth_next_stack and
#                 height_current > height_next_stack):
                
                    
#                     meets_criteria = True
#                     break

#         if meets_criteria:
#             valid_disks.append(value)
#     return f"valid_disks: {valid_disks}"

# res = stacks([[2,1,2],[3,2,3],[2,2,8],[2,3,4],[1,3,1],[4,4,5]])
# print(res)
# print("----------------------------------------------------------")


def stacks(x):
    #sort stacks in descending order
    sort_x = sorted(x, reverse=True)
    print(f"sorted stacks: {sort_x}")
    
    valid_disks = [] 

    for index, current_stack in enumerate(sort_x):
        print(f"index:{index},current:{current_stack}")
        meets_criteria = True
        
        #comparing the current stack with the next stacks
        for next_stack in sort_x[index+1:]:
            #print(f"next_stack: {next_stack}")
            if (current_stack[0] <= next_stack[0] or  #comparing widths
                current_stack[1] <= next_stack[1] or  #comparing depths
                current_stack[2] <= next_stack[2]):   #comparing height
                meets_criteria = False
                break  

        if meets_criteria:
            valid_disks.append(current_stack)
    
    return f"Valid disks: {valid_disks}"

# Example input
res = stacks([[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]])
print(res)

#Worst Case Time Complexity : O(n)raise to 2 , for every element of outer loop , the inner loop runs for n times.
#Worst Case Space Complexity : O(n) , all the elements of the initial_stack "stacks([[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]])"
# were used to identify the outcome.


    
            
    
    
print("----------------------")

import random
from datetime import datetime

class CovidTesting:
    def __init__(self,total_patients):
        self.total_patients= total_patients
        self.patients = list(range(1,total_patients+1))
        #print(f"my list {self.patients}")
        self.random_4=[]
        self.patients_dates={} #empty dict to store the dates of the patients
        
    #function to select 1 random number out of 5 (patient_id)
    def select_random_patients(self):
        for i in range(0,self.total_patients,5): #create a set of 5 numbers
            self.random_4.append(random.choice(self.patients[i:i+5]))#choose a random patient out of eveery 5 numbers.
        return self.random_4
    
    #function to assign dates to each patient_id
    def assign_dates(self):
        dates = datetime.today().strftime('%Y-%m-%d')
        for patient_id in self.random_4:
            self.patients_dates[patient_id]=dates
        return self.patients_dates.values()
    
covid = CovidTesting(20)
print(covid.select_random_patients())
print(covid.assign_dates())      

#Worst Case Time Complexity: O(n) we are generating 20 patients where n=20 which is total no.of patients, self.patients is storing all the patien_ids 
#which takes O(n) time
#Worst Case Space Complexity: O(4)  beause we are storing "4" patient_id and their dates for each block of 5 numbers.
            
    
# class CovidTesting:
#     def __init__(self):
#         self.patients=[]
#         self.random_4=[]
#         self.patients_dates={}
           
#     def set_total_patients(self,total_patients):
#         self.patients=list(range(1,total_patients+1))
    
#     def select_random_patients(self):
#         for i in range(0,len(self.patients),5):
#             self.random_4.append(random.choice(self.patients[i:i+5]))
#         return self.random_4
    
#     def assign_dates(self):
#         dates = datetime.today().strftime('%Y-%m-%d')
#         for patient_id in self.random_4:
#             self.patients_dates[patient_id]=dates
#         return self.patients_dates.values()

# covid = CovidTesting()
# print(covid.set_total_patients(20))
# print(covid.select_random_patients())
# print(covid.assign_dates())




# x=list(range(1,21))
# print(x)

# random_4=[]
# for i in range(0,20,5):
#     #print(i)
#     #print([i,i+5])
#     #print(x[i:i+5])
#     random_4.append(random.choice(x[i:i+5]))
# print(random_4)

# patient_dates={}
# dates = datetime.today().strftime('%Y-%m-%d')
# for patient_id in random_4:
#     patient_dates[patient_id]= dates
# print(patient_dates.values())

    

print("---------------------")

#cartesian-cordinates (x,y)
#output return the number of squares 
#x=[[[0,0],[0,1],[1,1],[1,0]], [[2,1],[2,0],[3,1],[3,0]], [[3,1],[3,0],[4,1],[4,0]]]
def no_of_squares(x):
    x = [tuple(point) for square in x for point in square]
    print(x)
    point_set = set(x)
    print(point_set) # removing the duplicates
    squares=0
    for i in range(0,len(x)):
        for j in range(i+1,len(x)):
            #print(f"i = {i}, j = {j} => x[i] = {x[i]}, x[j] = {x[j]}")
            p1=x[i]
            p2=x[j]
            
            if (p1[0] != p2[0] and p1[1] != p2[1]):# calculating coordinates of first 2 corners "P1 & P2"
                #(to form diagonal of square if they have different x&y cordinates)
                    p3 = (p1[0], p2[1]) #claculating the co-ordnates of other 2 corners "P3 & P4"
                    p4 = (p2[0], p1[1])
                    if p3 in point_set and p4 in point_set:
                        squares += 1
    squares//=5
    return f"no.of squares:{squares}"

res = no_of_squares([[[0,0],[0,1],[1,1],[1,0]], [[2,1],[2,0],[3,1],[3,0]], [[3,1],[3,0],[4,1],[4,0]]])
print(res)          
#Worst Case Time Complexity : O(n)raise to 2, for every element of outer loop , the inner loop runs for n times.
#Worst Case Space Complexity: O(n), all the elements within the list were used to find the outcome.

