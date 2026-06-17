import subprocess

print("Basit Ağ Tarama Aracı")
print("-" * 25)

ag = input("Ağ adresini gir (Örnek: 192.168.1): ")

print("\nTarama başlıyor...\n")

for i in range(1, 255):
    ip = f"{ag}.{i}"

    sonuc = subprocess.run(
        ["ping", "-n", "1", ip],
        capture_output=True,
        text=True
    )

    if "TTL=" in sonuc.stdout:
        print(f"[AKTİF] {ip}")

print("\nTarama tamamlandı.")
