import os
from dotenv import load_dotenv

# 1. Load API Key
load_dotenv()

from app.graph.workflow import native_care

def run():
    print("\n--- NativeCare AI Live ---")
    print("Type 'exit' or 'quit' to stop.\n")
    
    while True:
        try:
            user_query = input("You: ")
            
            if user_query.lower().strip() in ['exit', 'quit']:
                print("Goodbye!")
                break
                
            if not user_query.strip():
                continue
                
            result = native_care.invoke({"query": user_query})
            print(f"AI: {result['response']}\n")
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            if "429" in str(e):
                print("\n[!] Quota Exceeded: The Free Tier limit has been reached. Please wait 60 seconds or swap your API Key.\n")
            else:
                print(f"\n[!] Error: {e}\n")


if __name__ == "__main__":
    run()
