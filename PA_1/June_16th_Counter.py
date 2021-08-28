
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 19:10:25 2021

@author: Howe Wang

This following code is created to add step counter to assess time complexity and total steps of PA_1 source code
"""

from operator import itemgetter

def distance_calculation(a_coordinate, b_coordinate,count):
    #Calculate distance between two points using Euclidean_distance
    Euclidean_distance = ((a_coordinate[0]-b_coordinate[0])**2+(a_coordinate[1]-b_coordinate[1])**2)**(1/2)
    count += 1
    return (Euclidean_distance, count)
    
#testing:
#print(distance_calculation([1,2],[3,4]))

def calculate_all_distances(P, a_coordinate, b_coordinate,shortest_distance, count):
    #calculate distance across all coordinate combinations in this list
    if len(P)>=2 and len(P)<3: #calculate distance at lower bottom of 
        distance=distance_calculation(P[0],P[1],count)
        count += 1
        if distance<shortest_distance: #compare the calculated distance to the current shortest distance
            shortest_distance = distance
            a_coordinate = P[0]
            b_coordinate = P[1]
            count += 1
    else:
        for i in range(len(P)-1):#loop through the P of points and cover each combination of coordinates
            for j in range(i+1,len(P)):
                distance = distance_calculation(P[i],P[j],count)
                count += 1
                if  distance_calculation(P[i], P[j],count) < shortest_distance:
                    shortest_distance = distance
                    a_coordinate = P[i]
                    b_coordinate = P[j]
                    count += 1
                
    return(a_coordinate, b_coordinate,shortest_distance, count)
 
#This method above could have been the method to satisfy the question, but we can instead apply divide and conquer          
#question: My question  here is the worst case for loop in n^2, at some point in the code we do trigger this n^2 big Oh, would that not slow
#down the overall program and drag our divide and conquer to big oh n^2?

def panel(P, middle_point,a_coordinate, b_coordinate,shortest_distance, count): 
    #calculate short distance in the range of panel near the middle point in each partition
    #question here is maybe we can introduce another partition loop here? right now this is n^2 for time complexity
    included_list = []
    for points in P:
    #here we include every points lie in between the range of current shortest distance next to the middle point
        if points[0] <= P[middle_point][0]+int(shortest_distance[0]) and points[0] >= P[middle_point][0]-int(shortest_distance[0]):
            included_list.append(points)
            count += 1

        else:
            break
            
    sorted(included_list, key=lambda included_list: (included_list[0])) #sort all the points within the range based on x axis value
    count += 1
    for i in range(len(included_list)-1):
        for j in range(i+1, len(included_list)):
        # if the calculated distance is shorter than the shortest distance, reset the shortest coordinate pair and shortest distance
            if distance_calculation(included_list[i], included_list[j],count) < shortest_distance:
                a_coordinate = included_list[i]
                b_coordinate = included_list[j]
                shortest_distance = distance_calculation(included_list[i], included_list[j],count)
                count += 1
    
    # test: print(a_coordinate, b_coordinate,shortest_distance)
    return(a_coordinate, b_coordinate,shortest_distance,count)

def compare(P,a_coordinate, b_coordinate,shortest_distance,count):
    #compare distance across left right and panel results
    P_sorted = sorted(P, key=itemgetter(0))
    if len(P) <= 3: #use direct distance calculation when length of points is less or equal to 3
        return (calculate_all_distances(P,a_coordinate, b_coordinate, shortest_distance,count))
        count += 1
    else:
        #else divide the points between left and right based on x axis value
        middle_point = len(P)//2 
        left_side = P_sorted[:middle_point]
        right_side = P_sorted[middle_point:len(P)]
        count += 1
        
        #This is the part that took me the longest time to get correct logic, in the end I opted for a sequential analysis:
        #start with pair 0 and 1 in the P, calculate left first, generate a new set of shortest coordinate pair and distance
        #feed that results as parameters to right side calculation, update if needed, then in the end, feed that parameter
        #to panel section calculation, in the end, if we have shorter distance in any step, we will update shortest coordinate
        #pair and distance
        a_coordinate, b_coordinate,shortest_distance,count = compare(left_side,a_coordinate, b_coordinate, shortest_distance,count)
        a_coordinate, b_coordinate,shortest_distance,count = compare(right_side,a_coordinate, b_coordinate,shortest_distance,count)
        a_coordinate, b_coordinate,shortest_distance,count = panel(P, middle_point,a_coordinate, b_coordinate,shortest_distance,count)    
        
    #test:print(a_coordinate, b_coordinate,shortest_distance)
    return(a_coordinate, b_coordinate, shortest_distance, count)

def main(P,m):
    count = 0
    counter = 0
    result = []
    if m <= len(P)//2:
        while counter < m:
           outcome = compare(P, P[0], P[1], distance_calculation(P[0],P[1],count),count)
           result.append(outcome)
           P = [points for points in P if points not in (outcome[0],outcome[1])]
           counter += 1
    print ("Total input of pairs are:",len(P))
    print ("The shortest",m, "pairs in the list of points, the distance between them and the number of steps are:")
    for n in sorted(result, key=itemgetter(2)): #not sure why I have to sort here, otherwise the shortest and second shortest are in reverse order
        print(n)
        #return count
    #print(count)
    #deduct the current pair from the list
    #re run the program
    #counter +=1

#P = [(-343, -7), (-216, -6), (-125, -5), (-64, -4), (-27, -3), (993, 176), (693, 817), (418, -676), (-266, -531), (-179, -874), (-926, -332), (-379, 757), (-8, 183), (-991, 262), (880, 978), (-346, 528), (-258, -852), (-41, -124), (806, 901), (-189, -707), (393, -95), (905, -461), (127, -367), (-236, -204), (-527, 538), (-519, 552), (259, 330), (506, -730), (818, 821), (337, 283), (856, -879), (-511, 907), (-450, -145), (960, -344), (237, 338), (-38, -236), (-142, -238), (-95, 941), (-920, 764), (-464, 506), (-506, 636), (-153, 318), (-537, 826), (322, -616), (134, 561), (-13, 49), (-633, 179), (273, 289), (559, -67), (825, -477), (220, 830), (595, 736), (-329, 783), (447, 428), (451, 473), (929, 4), (281, -1000), (-695, 714), (-272, 15), (353, -92), (718, 3), (-697, -320), (-308, 304), (-46, -21), (464, -456), (395, -240), (-563, 569), (-126, 483), (150, -397), (-277, -522), (955, 960), (906, -576), (-960, 710), (37, -12), (-785, -988), (875, 311), (-538, -288), (-21, -836), (-961, -88), (-355, -211), (171, 835), (859, -420), (-300, -252), (178, -751), (385, 254), (-808, -114), (-895, -453), (-574, 167), (330, -750), (-496, -386), (-17, -416), (-756, -195), (832, 36), (-566, 123), (294, -449), (-366, 754), (431, 565), (9, -29), (-398, -214), (248, -236), (669, -700), (-794, -181), (-391, -855), (-45, -775), (391, -176), (694, -205), (569, 704), (-348, -110), (-669, 343), (226, 393), (223, -667), (763, 727), (739, -901), (-390, 771), (660, 393), (620, -71), (167, -624), (-325, 697), (584, 90), (-751, -574), (-73, -569), (938, -647), (-179, 598), (-681, 566), (-511, 520), (-258, -331), (13, 930), (656, -995), (907, -377), (634, -691), (89, -982), (-408, -816), (-544, 168), (804, -599), (-544, -401), (108, -30), (217, -166), (298, 405), (-773, -102), (-853, -370), (15, 629), (83, 944), (441, -484), (232, 381), (901, 80), (-819, -657), (-886, -665), (-691, 61), (-140, -271), (106, 20), (-156, 119), (726, -148), (-922, 448)]

#print ("The list of coordinates for testing is:", P)

#main(P,10)