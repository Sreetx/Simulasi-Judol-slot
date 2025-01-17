import random
import time

def spin_slot(balance):
    """
    Simulates an online slot game.
    
    Parameters:
        balance (int): The player's current balance.
    
    Returns:
        int: Updated balance after the spin.
    """
    cost_per_spin = 10  # Biaya setiap putaran
    winnings = [0, 5, 10, 50, 100, 1000]  # Kemungkinan hasil kemenangan
    probabilities = [0.5, 0.3, 0.1, 0.05, 0.04, 0.01]  # Peluang untuk menang (kecil banget!)

    if balance < cost_per_spin:
        print("Saldo habis! Anda tidak bisa bermain lagi.")
        return balance

    print("🎰 Memutar slot...")
    time.sleep(2)

    result = random.choices(winnings, probabilities)[0]
    balance -= cost_per_spin
    balance += result

    if result > 0:
        print(f"✨ Selamat! Anda menang {result} koin.")
    else:
        print("💸 Tidak ada kemenangan kali ini. Coba lagi!")

    return balance


def play_judol():
    """
    Simulates a series of slot spins with a starting balance.
    """
    print("🔥 Selamat datang di Judol! Kaya instan? Atau gali kuburanmu sendiri?")
    balance = 100  # Saldo awal
    while balance > 0:
        print(f"\nSaldo Anda: {balance} koin")
        choice = input("Mau main? Ketik 'spin' untuk putar atau 'stop' untuk berhenti: ").lower()

        if choice == 'spin':
            balance = spin_slot(balance)
        elif choice == 'stop':
            print(f"Anda berhenti dengan saldo {balance} koin. Bijaklah dalam mengambil keputusan!")
            break
        else:
            print("Input tidak valid. Ketik 'spin' atau 'stop'.")
    
    if balance == 0:
        print("Anda bangkrut. Judi bukan solusi! 🤷‍♂️")

# Main Program
play_judol()
