import random
import time

def spin_slot(balance, spins):
    """
    Simulates multiple spins of an online slot game.
    """
    cost_per_spin = 10  # Cost per spin
    winnings = [0, 5, 10, 50, 100, 1000]  # Possible winnings
    probabilities = [0.5, 0.3, 0.1, 0.05, 0.04, 0.01]  # Chances to win

    for spin in range(1, spins + 1):
        if balance < cost_per_spin:
            print(f"💀 Saldo habis! Kalo nggak sadar-sadar, gitu deh, ya. Mulai gali kubur sendiri sekarang. 🚜")
            break

        print(f"🎰 Putaran ke-{spin}... (Saldo: {balance} koin)")
        time.sleep(0.5)

        result = random.choices(winnings, probabilities)[0]
        balance -= cost_per_spin
        balance += result

        if result > 0:
            print(f"✨ Wow, menang {result} koin. Sedikit doang sih, ya, emangnya bisa jadi kaya segitu?")
        else:
            print("💸 No win. Kalah lagi, mungkin kamu memang dilahirkan untuk gitu. 🤷‍♂️")

    return balance


def play_judol():
    """
    Main function for playing the Judol slot game.
    """
    print("🔥 Selamat datang di Penggali Kuburan Otomatis! Mau kaya instan? Siap-siap buat rugi berat!")
    while True:
        try:
            balance = int(input("Masukkan saldo awal Anda: "))
            spins = int(input("Masukkan jumlah putaran yang ingin dilakukan: "))
            if balance <= 0 or spins <= 0:
                print("Input harus angka positif! Jangan sok-sokan deh.")
                continue
        except ValueError:
            print("Gimana sih, ngasal banget! Masukkan angka yang bener!")
            continue

        # Start spinning
        final_balance = spin_slot(balance, spins)

        print(f"\nHasil akhir: Saldo Anda adalah {final_balance} koin.")
        if final_balance == 0:
            print("💀 Yahahah dongo!.")
            print("💀 Saldo habis. Gali kuburan makin dalam, yuk!")
        else:
            print("🎉 Masih ada saldo? Awas, jangan kelewat nyaman, nanti malah makin parah.")

        # Option to play again or quit
        choice = input("\nMau main lagi? (ya/tidak): ").lower()
        if choice != 'ya':
            print("Hidup bukan buat main judi terus, bro. Cobalah jadi manusia seutuhnya!")
            break


# Main Program
play_judol()
