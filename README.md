

🎓 Student Performance Prediction with Decision Trees
Selamlar! Bu projede, öğrencilerin akademik başarılarını 
(Performance Index) hangi faktörlerin (çalışma saati, uyku düzeni, derslere katılım vb.) 
ne derece etkilediğini tahmin etmeye çalışan bir makine öğrenmesi modeli geliştirdim.

Sadece bir tahmin modeli kurmakla kalmayıp, GridSearchCV ile hiperparametre optimizasyonu yaparak modelin en iyi halini bulmaya çalıştım.

🧐 Projenin Hikayesi ve Analiz
Veri setini incelerken öğrencilerin alışkanlıklarının performans üzerindeki etkisini merak ettim. Kod akışında şu adımları izledim:

Veri Ön İşleme: "Extracurricular Activities" gibi kategorik verileri makinenin anlayacağı dile (0 ve 1) çevirdim.

Model Seçimi: En son öğrendiğim konu olduğu için DecisionTreeRegressor modelini tercih ettim.

İnce Ayar (Tuning): Modelin sadece veriyi ezberlemesini (overfitting) engellemek ve en iyi skoru yakalamak için; max_depth, 
min_samples_split ve criterion gibi hiperparametreleri 5 katlı çapraz doğrulama (GridSearchCV) ile optimize ettim.

🛠️ Kullanılan Teknolojiler
Python 3.x

Pandas & NumPy: Veri manipülasyonu için.

Scikit-Learn: Makine öğrenmesi algoritması ve metrikler için.

Matplotlib & Seaborn: Veri setini görsel olarak anlamak için (kod içerisinde opsiyonel olarak bırakıldı).

📊 Sonuçlar
Modelin başarısını ölçmek için regresyon dünyasının iki önemli metriğine odaklandım:

MAE (Mean Absolute Error): Tahminlerin gerçek değerlerden ortalama ne kadar saptığını gösterir.

R² Score: Modelin verideki değişkenliği ne kadar iyi açıkladığını belirtir. (Skorun 1.0'a ne kadar yakınsa o kadar iyi!)