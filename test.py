from tasks import add

result = add.delay(5, 10)

print("Task ID:", result.id)