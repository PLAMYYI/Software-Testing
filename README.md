# Software-Testing
การเขียนอัลกอริทึมและทำการทดสอบด้วย Unit Test โดยใช้ pytest
พร้อมตรวจสอบ Test Coverage เพื่อให้มั่นใจว่าโค้ดถูกทดสอบครบทุกส่วน

1. โครงสร้าง
Software-Testing
- src ( เก็บไฟล์อัลกอริทึม )
- tests ( เก็บไฟล์ test )
- README.md

3. โจทย์
- Alternating Characters :
หาจำนวนตัวอักษรที่ต้องลบออกเพื่อไม่ให้มีตัวอักษรซ้ำติดกัน
- Caesar Cipher :
เข้ารหัสข้อความโดยเลื่อนตัวอักษรตามจำนวนที่กำหนด
- Funny String :
ตรวจสอบว่าความต่างของ ASCII จากหน้าไปหลังและหลังไปหน้ามีค่าเท่ากันหรือไม่
- Grid Challenge :
เรียงตัวอักษรในแต่ละแถว และตรวจสอบว่าคอลัมน์เรียงลำดับถูกต้องหรือไม่
- Two Characters :
เลือกตัวอักษร 2 ตัวมาสร้าง pattern แบบสลับกัน และหาความยาวสูงสุด

3. วิธีรันโปรแกรมทดสอบ
- ติดตั้ง : pip install pytest pytest-cov
- รัน Unit Test: pytest
- Test Coverage : pytest --cov=src --cov-report=term-missing

** if __name__ == "__main__" ถูกกำหนด # pragma: no cover
เพื่อไม่ให้นับรวมใน Test Coverage **
