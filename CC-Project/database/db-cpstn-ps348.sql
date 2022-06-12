BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "user" (
	"user_id"	INTEGER NOT NULL,
	"full_name"	VARCHAR(50),
	"email"	VARCHAR(50),
	"password"	VARCHAR(50),
	PRIMARY KEY("user_id")
);
CREATE TABLE IF NOT EXISTS "kantong" (
	"kantong_id"	INTEGER NOT NULL,
	"gambar"	TEXT,
	"hasil_prediksi"	VARCHAR(25),
	"deskripsi_user"	VARCHAR(100),
	PRIMARY KEY("kantong_id")
);
INSERT INTO "user" ("user_id","full_name","email","password") VALUES (1,'Hadid Ray Aldy','hadid@gmail.com','Hadid123'),
 (2,'Yusuf Irsyaduddin','yusuf@gmail.com','Yusuf123'),
 (3,'Ridho Ajiraga Jagiswara','ridho@gmail.com','Ridho123'),
 (4,'Maria Febriyanti Simanjuntak','maria@gmail.com','Maria123'),
 (5,'Naufaliando Yudo Kusumo','naufal@gmail.com','Naufal123'),
 (6,'Abdun Nafi','abdu@gmail.com','Abdu123'),
 (7,'user','user@gmail.com','User123');
INSERT INTO "kantong" ("kantong_id","gambar","hasil_prediksi","deskripsi_user") VALUES (1,'https://www.mentimun.co.id/images/store/235LGCocacola_slim_kaleng__250_ml.jpg','Metal','Kaleng Coca-Cola 330ml'),
 (2,'https://cf.shopee.co.id/file/f88cb44b70603f35fce49fc922ee0767','Plastic','Botol Aqua 1Liter'),
 (3,'https://example/image-01.jpg','Paper','Buku bekas'),
 (4,'https://example/image-02.jpg','Cardboard','Kardus Bekas Teh Gelas 160ml x 24 cup'),
 (5,'https://example/image-03.jpg','Glass','Botol Kaca Teh Botol Sosro 1,2Liter'),
 (6,'https://example/image-04.jpg','Trash','Kursi Kayu Bekas'),
 (7,'https://example/image-05.jpg','Glass','Kaca Mobil Bekas'),
 (8,'https://example/image-06.jpg','Trash','Ban Motor Bekas'),
 (9,'https://example/image-07.jpg','Metal','Knalpot Motor Bekas');
COMMIT;
