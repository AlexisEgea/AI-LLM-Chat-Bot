from src.model.model_factory import ModelFactory

if __name__ == '__main__':
    model = ModelFactory("gpt-4o-mini").get_model()

    try:
        while True:
            message = input("User: ")
            response = model.get_response(message)
            print(f"AI: {response}")

    except KeyboardInterrupt:
        total_cost = model.total_cost
        print('\n')
        print(f"Conversation Cost: {format(total_cost, '.10f')}$")
        print('\n')
        # Create log file to keep conversation
        print(f'Conversation log: ')
        print(model.memory)
