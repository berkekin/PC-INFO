EN:

This code snippet showcases a Python application crafted with the tkinter library to construct a GUI (Graphical User Interface), aimed at rendering an array of system information on a user's computer. At its core, the application leverages the tkinter library for the graphical user interface, psutil for system information access, platform for retrieving hardware details like the CPU model, and subprocess for executing external commands, specifically to gather GPU information through NVIDIA's System Management Interface (SMI).

The application is encapsulated within the SystemInfoApp class, which upon initialization, sets up the main application window, titles it "System Information", and then proceeds to dynamically create tabs for displaying specific categories of system information: GPU, CPU, RAM, Disk, and Network. Each tab is meticulously designed to present data in a clear, user-friendly manner.

GPU Information: Utilizes nvidia-smi command to fetch details such as the GPU name, load, memory (total, used, free), temperature, power draw, and fan speed. This is particularly useful for users with NVIDIA GPUs to monitor their hardware's performance and health.
CPU Information: Gathers data including the CPU model, number of physical and logical cores, maximum and current frequency, and overall CPU usage percentage. This information helps users understand their processor's capabilities and current load.
RAM Information: Shows details on total, available, used RAM, and usage percentage, along with swap memory information. It gives users insight into their system's memory usage and availability, which is crucial for performance management.
Disk Information: Displays the total, used, and free disk space, along with disk usage percentage, read and write counts, and the amount of data read and written. This section is essential for users to monitor their storage utilization and performance.
Network Information: Provides details on network interfaces, including status, speed, IP addresses (IPv4 and IPv6), MAC address, packets sent and received, and bytes sent and received. This tab offers users a comprehensive view of their network connections and activity.
The application's dynamic nature is highlighted by its ability to automatically update information at regular intervals, ensuring users have access to real-time data regarding their system's performance. This makes the application an invaluable tool for monitoring, troubleshooting, and ensuring the optimal operation of a computer system.



TR:
Bu kod parçacığı, kullanıcıların bilgisayarlarındaki çeşitli sistem bilgilerini sunmayı amaçlayan, tkinter kütüphanesi kullanılarak hazırlanmış bir GUI (Grafik Kullanıcı Arayüzü) içeren Python uygulamasını sergilemektedir. Uygulama, grafiksel kullanıcı arayüzü için tkinter kütüphanesini, sistem bilgilerine erişim için psutil'ı, CPU modeli gibi donanım detaylarını elde etmek için platformu ve özellikle NVIDIA'nın Sistem Yönetim Arayüzü (SMI) aracılığıyla GPU bilgilerini toplamak için subprocessı kullanır.

Uygulama, SystemInfoApp sınıfı içinde kapsüllenmiş olup, başlatıldığında ana uygulama penceresini kurar, "System Information" başlığını atar ve ardından spesifik sistem bilgileri kategorilerini göstermek için dinamik olarak sekmeler oluşturur: GPU, CPU, RAM, Disk ve Ağ. Her sekme, verileri açık ve kullanıcı dostu bir şekilde sunacak şekilde titizlikle tasarlanmıştır.

GPU Bilgisi: nvidia-smi komutunu kullanarak GPU adı, yük, bellek (toplam, kullanılan, boş), sıcaklık, güç çekişi ve fan hızı gibi detayları getirir. Bu, NVIDIA GPU'ları olan kullanıcıların donanımlarının performansını ve sağlığını izlemeleri için özellikle yararlıdır.
CPU Bilgisi: CPU modeli, fiziksel ve mantıksal çekirdek sayısı, maksimum ve mevcut frekans ve genel CPU kullanım yüzdesi dahil olmak üzere verileri toplar. Bu bilgi, kullanıcılara işlemcilerinin kapasiteleri ve mevcut yükü hakkında bilgi verir.
RAM Bilgisi: Toplam, kullanılabilir, kullanılan RAM ve kullanım yüzdesi ile birlikte takas belleği bilgilerini gösterir. Kullanıcılara sistemlerinin bellek kullanımı ve mevcudiyeti hakkında içgörü sağlar, bu da performans yönetimi için kritik öneme sahiptir.
Disk Bilgisi: Toplam, kullanılan ve boş disk alanı ile birlikte disk kullanım yüzdesi, okuma ve yazma sayıları ve okunan ve yazılan veri miktarını gösterir. Bu bölüm, kullanıcıların depolama kullanımını ve performansını izlemeleri için temeldir.
Ağ Bilgisi: Ağ arayüzleri hakkında durum, hız, IP adresleri (IPv4 ve IPv6), MAC adresi, gönderilen ve alınan paketler ve gönderilen ve alınan baytlar dahil detaylar sağlar. Bu sekme, kullanıcılara ağ bağlantıları ve etkinlikleri hakkında kapsamlı bir görünüm sunar.
Uygulamanın dinamik doğası, bilgileri düzenli aralıklarla otomatik olarak güncelleyerek, kullanıcılara sistemlerinin performansı hakkında gerçek zamanlı verilere erişim sağlamasıyla vurgulanır. Bu, uygulamayı bilgisayar sistemlerinin izlenmesi, sorun giderilmesi ve optimal çalışmasının sağlanması için paha biçilmez bir araç haline getirir.
