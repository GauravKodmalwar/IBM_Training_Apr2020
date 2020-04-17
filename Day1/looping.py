
for k in range(5):
    for i in range(1,20):
        if i % 5 == 0:
            print(i)
            break
        elif i % 2 == 0:
            continue
        print(i)

    print("outside of loop")


import sys
print(sys.path)
sys.path.append("F:\\PythonIBMTraining\\PythonTraining\\Day1")
import session1
