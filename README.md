# GStreamer-OpenCV
OpenCV read stream thought GStreamer > deploy with python

## Effect of Gstreamer:

Gstreamer cho phép dòng stream liên tục và không bị đứt đoạn, tức là luôn cùng thời gian với thời gian thực (vượt qua các điểm bị nghẽn).

Link: [Mulitmedia trong Linux](https://zxc232.wordpress.com/2009/12/21/multimedia-trong-linux-b%E1%BB%95-xung-va-h%E1%BA%BFt/)

**Codec** (viết tắt của en coder/ decoder)là các phần mềm/thuật toán/công nghệ dùng để mã và giải mã (có nén hoặc không) dữ liệu multimedia như nói trên.

**Multimedia Format**: sau khi mã hóa, dữ liệu multimedia được lưu thành các file có định dạng (format) khác nhau. Một file ảnh có thể lưu dưới dạng file jpg, png, bmp, … Một đoạn phim thường gồm ba loại dữ liệu: video, audio và metadata để đồng bộ hình với tiếng. Ba loại dữ liệu đó được lưu chung trong một loại format gọi là media container format (ví dụ avi). Nhiều loại codec khác nhau có thể lưu file cùng một format avi, tất nhiên là chất lượng phim tùy theo codec.
Một cơ chế xử lý dữ liệu multimedia (Multimedia framework – MMF) là một hệ thống phần mềm xử lý các dữ liệu multimedia trên máy tính hoặc mạng máy tính theo một cơ chế nào đó. Hệ thống gồm một giao diện lập trình ứng dụng API, các module hỗ trợ các loại codecs, container formats và hỗ trợ các giao thức truyền dẫn luồng âm thanh, video (streaming media) qua mạng.
MMF dùng làm hệ thống nền (back-end) cho các ứng dụng chơi nhạc, video, các phần mềm biên tập âm thanh và video, các ứng dụng videoconferencing và các phần mềm multimedia khác.
Một vài MMF phổ biến:
**GStreamer**: một MMF nguồn mở chạy được trên Linux, Solaris, Mac, Windows.
 
**GStreamer** chia các công đoạn xử lý thành các bộ phận (element). Các bộ phận nối với nhau bằng các đường ống (pipeline) có đầu ra (source pad) và đầu vào (sink pad). Trong hình trên là ví dụ chơi một file MP3: bộ phận File đọc file từ ổ cứng rồi chuyển cho bộ phận giải mã (Decoder). Decoder chuyển dữ liệu số thành mã xung (Pulse-code Modulation). Mã xung theo đường ống chuyển cho bộ phận ALSA driver để từ đó đưa ra loa.
Mỗi bộ phận (chức năng) của GStreamer được lập trình dưới dạng plugin (phần mềm bổ xung) tạo nên các thư viện dùng chung. Hiện tại có ba bộ plugin là Good, Bad và Ugly. Good plugins gồm các plugin chất lượng cao, tuân theo giấy phép nguồn mở LGPL, đã được kiểm định đầy đủ. Bad plugins gồm các plugin chưa hoàn chỉnh về mặt nào đó như Good (chất lượng chưa cao, hoặc chất lượng cao nhưng còn thiếu một cái gì đó, …). Ugly plugins là các plugins chất lượng tốt nhưng có vấn đề về bản quyền.
