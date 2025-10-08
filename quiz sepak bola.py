def jalankan_kuis():
    skor = 0
    pertanyaan = [
        {
            "pertanyaan": "Siapakah pemain yang memenangkan Ballon d'Or terbanyak?",
            "pilihan": ["Lionel Messi", "Cristiano Ronaldo", "Michel Platini", "Johan Cruyff"],
            "jawaban": "Lionel Messi"
        },
        {
            "pertanyaan": "Berapa lama biasanya satu babak dalam pertandingan sepak bola?",
            "pilihan": ["30 menit", "45 menit", "60 menit", "90 menit"],
            "jawaban": "45 menit"
        },
        {
            "pertanyaan": "Tim nasional mana yang paling banyak memenangkan Piala Dunia?",
            "pilihan": ["Brasil", "Jerman", "Italia", "Argentina"],
            "jawaban": "Brasil"
        },
        {
            "pertanyaan": "Liga sepak bola mana yang dianggap paling kompetitif di dunia?",
            "pilihan": ["La Liga", "Serie A", "Premier League", "Bundesliga"],
            "jawaban": "Premier League"
        },
        {
            "pertanyaan": "Siapakah satu-satunya pemain yang memenangkan tiga Piala Dunia?",
            "pilihan": ["Diego Maradona", "Pelé", "Zinedine Zidane", "Franz Beckenbauer"],
            "jawaban": "Pelé"
        }
    ]

    print("===================================")
    print("        ⚽ KUIS SEPAK BOLA ⚽       ")
    print("===================================\n")

    for i, soal in enumerate(pertanyaan):
        print(f"Soal {i + 1}: {soal['pertanyaan']}")
        for j, pilihan in enumerate(soal['pilihan']):
            print(f"   {j + 1}. {pilihan}")

        jawaban_pengguna = input("Jawaban Anda (ketik nomor pilihan): ")

        try:
            jawaban_pengguna = int(jawaban_pengguna)
            if 1 <= jawaban_pengguna <= len(soal['pilihan']):
                if soal['pilihan'][jawaban_pengguna - 1] == soal['jawaban']:
                    print("✅ Benar!\n")
                    skor += 1
                else:
                    print(f"❌ Salah. Jawaban benar: {soal['jawaban']}\n")
            else:
                print("⚠️ Pilihan tidak valid. Soal dilewati.\n")
        except ValueError:
            print("⚠️ Input tidak valid. Soal dilewati.\n")

    print("===================================")
    print(f"Kuis selesai! Skor Anda: {skor}/{len(pertanyaan)}")
    print("===================================")


# Jalankan program
jalankan_kuis()
