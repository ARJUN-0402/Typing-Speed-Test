import time
import random

# Sentences by difficulty
sentences = {
    "easy": [
        "The sun is shining bright",
        "I love to code in Python",
        "Typing games are fun"
    ],
    "medium": [
        "Artificial Intelligence is the future of technology",
        "Typing speed tests help improve productivity and accuracy",
        "Python sockets can create chat applications with ease"
    ],
    "hard": [
        "The quick brown fox jumps over the lazy dog multiple times",
        "Synchronization and multithreading improve program efficiency",
        "Debugging complex algorithms requires patience and focus"
    ]
}

leaderboard = {}  # Store scores by username


def calculate_wpm_and_accuracy(start_time, end_time, typed_text, target_text):
    elapsed_time = end_time - start_time
    words = typed_text.split()
    correct_words = sum(1 for tw, aw in zip(words, target_text.split()) if tw == aw)
    wpm = (len(typed_text.split()) / (elapsed_time / 60)) if elapsed_time > 0 else 0
    accuracy = (correct_words / len(target_text.split())) * 100
    return wpm, accuracy


def normal_mode(username, difficulty):
    total_wpm, total_accuracy = 0, 0
    print("\n--- Normal Mode: 3 Rounds ---\n")
    
    for i in range(3):
        target = random.choice(sentences[difficulty])
        print(f"Round {i+1}: Type this sentence →")
        print(f"👉 {target}\n")
        
        input("Press Enter when ready...")
        start = time.time()
        typed = input("Your typing: ")
        end = time.time()
        
        wpm, accuracy = calculate_wpm_and_accuracy(start, end, typed, target)
        total_wpm += wpm
        total_accuracy += accuracy
        
        print(f"⏱ Time: {end-start:.2f}s | ⚡ WPM: {wpm:.2f} | 🎯 Accuracy: {accuracy:.2f}%\n")
    
    avg_wpm = total_wpm / 3
    avg_accuracy = total_accuracy / 3
    print(f"\n✅ Final Result → Avg WPM: {avg_wpm:.2f}, Avg Accuracy: {avg_accuracy:.2f}%\n")
    
    leaderboard[username] = max(leaderboard.get(username, 0), avg_wpm)


def timed_mode(username, difficulty, duration):
    print(f"\n--- Timed Mode: {duration} seconds ---\n")
    total_wpm, total_accuracy, rounds = 0, 0, 0
    
    start_time = time.time()
    while time.time() - start_time < duration:
        target = random.choice(sentences[difficulty])
        print("Type this sentence →")
        print(f"👉 {target}\n")
        
        input("Press Enter when ready...")
        s = time.time()
        typed = input("Your typing: ")
        e = time.time()
        
        wpm, accuracy = calculate_wpm_and_accuracy(s, e, typed, target)
        total_wpm += wpm
        total_accuracy += accuracy
        rounds += 1
        
        print(f"⏱ Time: {e-s:.2f}s | ⚡ WPM: {wpm:.2f} | 🎯 Accuracy: {accuracy:.2f}%\n")
        
        if time.time() - start_time >= duration:
            break
    
    if rounds > 0:
        avg_wpm = total_wpm / rounds
        avg_accuracy = total_accuracy / rounds
    else:
        avg_wpm, avg_accuracy = 0, 0
    
    print(f"\n✅ Final Timed Result → Avg WPM: {avg_wpm:.2f}, Avg Accuracy: {avg_accuracy:.2f}%\n")
    leaderboard[username] = max(leaderboard.get(username, 0), avg_wpm)


def show_leaderboard():
    print("\n🏆 Leaderboard 🏆")
    print("-" * 30)
    for user, score in sorted(leaderboard.items(), key=lambda x: x[1], reverse=True):
        print(f"{user:<15} | {score:.2f} WPM")
    print("-" * 30)


def main():
    print("🎯 Typing Speed Test 🎯")
    username = input("Enter your username: ")
    
    while True:
        print("\nChoose difficulty → [easy / medium / hard]")
        difficulty = input("Difficulty: ").lower()
        if difficulty not in sentences:
            print("Invalid choice. Try again.")
            continue
        
        print("\nChoose mode → [1] Normal (3 Rounds) | [2] Timed (30s) | [3] Timed (60s)")
        choice = input("Enter choice: ")
        
        if choice == "1":
            normal_mode(username, difficulty)
        elif choice == "2":
            timed_mode(username, difficulty, 30)
        elif choice == "3":
            timed_mode(username, difficulty, 60)
        else:
            print("Invalid mode. Try again.")
            continue
        
        show_leaderboard()
        
        again = input("\nPlay again? (y/n): ").lower()
        if again != "y":
            break


if __name__ == "__main__":
    main()
