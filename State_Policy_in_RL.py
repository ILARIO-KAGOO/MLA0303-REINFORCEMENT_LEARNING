states= [(0,0),(0,1),(1,0),(1,1)]
actions={'up':(-1,0),'Down':(1,0),'left':(0,-1),'right':(0,1)}
policy={
  (0,0):'right',
  (0,1):'Down',
  (1,0):'right',
  (1,1):'up'
}
def get_next_state(state,action):
  next_state = (state[0]+actions[action][0],state[1]+actions[action][1])
  if next_state in states:
    return next_state
  return state
def get_action(state):
  return policy[state]

current_state =(0,0)
for i in range(3):
  action=get_action(current_state)
  next_state= get_next_state(current_state,action)
  print(f"Current state: {current_state},action:{action},Next state:{next_state}") 
  current_state=next_state