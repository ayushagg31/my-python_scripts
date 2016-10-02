import os

url = "https://www.google.co.in/imgres?imgurl=https%3A%2F%2Fi.ytimg.com%2Fvi%2FEDvE72Y4ckU%2Fmaxresdefault.jpg&imgrefurl=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DEDvE72Y4ckU&docid=68lHGdkzGe9tDM&tbnid=Hs0h-7kVPoy5rM%3A&w=1280&h=720&client=ubuntu&bih=587&biw=1366&ved=0ahUKEwiTu4SugLzPAhXBPI8KHSsbCzAQMwgfKAIwAg&iact=mrc&uact=8"
command = "wget "+ url
os.system(command)
