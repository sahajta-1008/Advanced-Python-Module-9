classmates=["Aarav","Priya","Rahul","Vishuddhi","Samkiti"]
print(len(classmates))
print(classmates[2:4])
classmates.append("Sahajta")
print("Adding Sahajta : ",classmates)
classmates.remove("Vishuddhi")
print("Removing Vishuddhi : ",classmates)
classmates.sort()
print("Alphabetical order : ",classmates)
classmates.reverse()
print("Reversed :",classmates)


dictionary={
    "Name":"Sahajta",
    "Age":11,
    "Height":5
}
print("Dictionary : ",dictionary)
print("Age : ",dictionary["Age"])
print("Height : ",dictionary.get("Height","Not Found"))


rollNo=[1,2,3,4,5]
names=["Prisha","Taanya","Tanaaya","John","Jonny"]
ans=dict(zip(rollNo,names))
print(ans)