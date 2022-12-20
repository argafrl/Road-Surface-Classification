import cv2

# Membuka perangkat video
cap = cv2.VideoCapture(0)

# Mendefinisikan codec dan menciptakan VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

while(cap.isOpened()):
    # Membaca frame dari perangkat video
    ret, frame = cap.read()
    if ret==True:
        # Menulis frame ke file video
        out.write(frame)

        # Menampilkan frame dalam jendela
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Menutup perangkat video dan file video
cap.release()
out.release()
cv2.destroyAllWindows()
# Dalam kode di atas, kita membuka perangkat video menggunakan cv2.VideoCapture(0), yang menunjukkan bahwa kita ingin menggunakan webcam default. Anda juga dapat menggunakan nomor indeks lain atau nama file video sebagai argumen untuk membuka perangkat video lain atau file video.

# Kemudian, kita mendefinisikan codec yang akan digunakan untuk menyimpan video ke dalam file dengan menggunakan fungsi cv2.VideoWriter_fourcc(). Dalam contoh ini, kita menggunakan codec 'XVID'. Anda dapat menggunakan codec lain yang tersedia di komputer Anda.

# Setelah itu, kita menciptakan objek cv2.VideoWriter yang akan digunakan untuk menulis frame ke file video. Kita memberikan nama file video yang akan kita simpan, codec yang telah kita definisikan, frame rate, dan ukuran frame sebagai argumen.

# Kemudian, kita masuk ke loop while dan membaca frame dari perangkat video menggunakan fungsi cap.read(). Jika frame telah berhasil dibaca, kita menuliskannya ke file video dengan menggunakan fungsi out.write() dan menampilkan frame ke layar menggunakan fungsi cv2.imshow().

# Setelah selesai merekam video, kita menutup perangkat video dan file video dengan menggunakan fungsi cap.release() dan out