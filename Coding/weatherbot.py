print("Tell me is it rainy or sunny or cloudy outside?")
view=input("User:")
if 'rainy' in view:
    print("You must carry the umbrella")
elif 'sunny' in view:
    print("No need to carry the umbrella")
elif 'cloudy' in view:
    print("tell me how much cloudy in percentage")
    cloudy=int(input("cloudy in %:"))
    sun=100-cloudy
    if(cloudy>sun):
        print("better to carry the umbrella")
    elif(cloudy<sun):
        print("No need to worry")
    elif(cloudy==sun):
       print("Good to maintain the umbrella")
