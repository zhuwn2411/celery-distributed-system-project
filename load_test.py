from tasks import add

for i in range(50):
    add.delay(i, i + 1)

print("Submitted 50 tasks")