from commands import ai_router

while True:

    command = input("You: ")

    result = ai_router.run(command)

    print(result)