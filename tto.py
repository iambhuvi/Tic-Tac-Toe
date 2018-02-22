
# coding: utf-8

# In[123]:


#Global DataStructures
#a dictionary to keep record of moves performed by player_1 and player_2
players_move={'player_1':[],'player_2':[]}
remaining_chances={'p1':5,'p2':4}
board=['','','','','','','','','']
#to print first time as our board print depends on the entires in the player_move and
# player_move will be empty intially hence no board get printes. so, we are using one time manual printig to print out board
inital_board_print=1


# In[124]:


def inital():
    #To display intial greeting and clear the datastructures
    print "Playing Board Has Counting From [0-8]\n"
    clr()


# In[125]:


def start():
    global players_move,remaining_chances
    inital()
    print_player_move()
    #current_chance=0  means player1 has chance otherwise player2
    current_chance=0
    
    while remaining_chances['p1']>0 or remaining_chances['p2']>0:
        #variables for sending moves to tto_input
        
        if current_chance==0 and remaining_chances['p1']>0:
            try :
                input_move1=int(raw_input('Enter your move player 1\t'))
            except:
            #Checking if user has inputed correctly
            
                print 'illegal input! Please enter a interger number only'.title() 
                continue
            
            #taking return of tto_input as string to check for illegal move condtion
            ret_stm1=str(tto_input(input_move1,'p1'))
            
            if'illegal move'== ret_stm1:
                print_player_move()
                print ret_stm1
                
            elif 'This game won by: p1'==ret_stm1:
                    print_player_move()
                    print ret_stm1
                    break
            else :
              #  print 'ret_stm1 is {x}'.format(x=ret_stm1)
                current_chance=1
                remaining_chances['p1']-=1
                print_player_move()
                print 'chances remaining for p1: {x}\n'.format(x=remaining_chances['p1']).title()
                
        
        elif current_chance==1 and remaining_chances['p2']>0:
            try:
                input_move2=int(raw_input('Enter your move player 2\t'))
            except:
            #Checking if user has inputed correctly
            
                print 'illegal input! Please enter a interger number only'.title() 
                continue
            
            #taking return of tto_input as string to check for illegal move condtion
            ret_stm2=str(tto_input(input_move2,'p2'))
            
            if 'illegal move'== ret_stm2:
                print_player_move()
                print ret_stm2
            elif 'This game won by: p2'==ret_stm2:
                    print_player_move()
                    print ret_stm2
                    break

            else :
                #print 'ret_stm2 is {x}'.format(x=ret_stm2)
                current_chance=0
                remaining_chances['p2']-=1
                print_player_move()
                print 'chances remaining for p2: {x}\n'.format(x=remaining_chances['p2'])

            
        else :
            
            print "In else of start()"
            break


# In[126]:


def tto_input(move_in,player_id):
    global players_move,remaining_chances
    #to check if move is out of range of the board
    if  move_in in range(0,9):
        pass
    else :
        return 'illegal move'
    
     #to check if the given move is already been present in previously given inputs
    if players_move['player_1'].count(move_in) or players_move['player_2'].count(move_in):
        return 'illegal move'
    
        
    if player_id=='p1':                                              
        players_move['player_1'].append(move_in)          
        return check_win(players_move['player_1'],player_id)       #sending update moves of player_1 to check_win
    elif player_id=='p2':
        players_move['player_2'].append(move_in)
        return check_win(players_move['player_2'],player_id)       #sending update moves of player_1 to check_win
    else:
        return 'Enter correct player id'

  


# In[127]:


def check_win(l,player_id):
    import itertools as it

    #win moves, created as tuples so that can't be modifed during program run.
    win_set=([0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6])  
    
    #To generate all possible size 3 permutation from player_move
    temp_perm_list=list(it.permutations(l,3))
    
    #checking if any of the permuation matches with the win_set element
    for element in win_set:
        for element_in_temp_perm_list in temp_perm_list:
            if set(element_in_temp_perm_list)==set(element): #Checking by making a set out of l, just used to sort the 'l' list an to type cast into set as to sort and not to modify the orginal list 'l
                return 'This game won by: {x}'.format(x=player_id)
            
            
    if len(l)==5 and player_id=='p1':
        print 'NO ONE WON THIS GAME!!'
           
    else:
       # print "IN check_win else"
      pass


# In[128]:


def clr(): 
    #To clear all inputs
    global players_move,remaining_chances,inital_board_print
    inital_board_print=1
    players_move['player_1']=[] 
   # print players_move['player_1']
    players_move['player_2']=[] 
   # print players_move['player_2']
    
    remaining_chances['p1']=5
    remaining_chances['p2']=4
    
    global board
    board=['BOX 0','BOX 1','BOX 2','BOX 3','BOX 4','BOX 5','BOX 6','BOX 7','BOX 8']    
    print 'all previuously given Entries have been cleared'.title()


# In[129]:


def print_player_move():
    #just for debugging
   # print players_move['player_1']
    #print players_move['player_2']
    
    #to print first time as our board print depends on the entires in the player_move and
# player_move will be empty intially hence no board get printes. so, we are using one time manual printig to print out board
    global inital_board_print
    if inital_board_print==1:
        inital_board_print=0
        show_board(0,'BOX 0')
        
    for element_in_player1 in players_move['player_1']:
        show_board(element_in_player1,'X')
    for element_in_player2 in players_move['player_2']:
        show_board(element_in_player2,'O')
    


# In[130]:


import os
def show_board(element,mark):
    global board
    os.system('clear')
    board[element]=mark
    print ('-------------------------------------------------')
    print ('|\t'+str(board[0])+'\t|\t'+str(board[1])+'\t|\t'+str(board[2])+'\t|\t')
    print ('-------------------------------------------------')
    print ('|\t'+str(board[3])+'\t|\t'+str(board[4])+'\t|\t'+str(board[5])+'\t|\t')
    print ('-------------------------------------------------')
    print ('|\t'+str(board[6])+'\t|\t'+str(board[7])+'\t|\t'+str(board[8])+'\t|\t')
    print ('-------------------------------------------------')
    


# In[131]:


def play():
    
        start()
        
        while True:
            play_in=raw_input("Do you want to play again !!!. enter Y/N".title())
            if play_in=='Y' or play_in=='y' or play_in=='yes':
                start()
            elif play_in=='N' or play_in=='n' or play_in=='no':
                break
        print "Thank for playing !!".upper()
            
        


# In[121]:


play()

