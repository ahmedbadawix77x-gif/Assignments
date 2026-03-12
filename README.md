# Event Management API - Task 2

This is the updated version of Assignment-1. المشروع ده اتطور عشان نستخدم الـ **Django REST Framework (DRF)** ونمشي على الـ Best Practices في الـ API design.

## Serializers
Switching to `ModelSerializer` was a game changer. وفر عليا كتابة كود كتير لأنه بيعمل **automated mapping** بين الـ Model والـ API Fields لوحده، وده بيخلي الـ code أنضف بكتير وأسهل في الـ maintenance.

## Logic & Validation
ضفت شوية Logic عشان أتأكد إن الداتا اللي داخلة سليمة:
- **Date Check**: الـ `start_date` لازم يكون قبل الـ `end_date` (منطقي جداً، مفيش Event بيبدأ بعد ما يخلص).
- **Whitespace Validation**: عملت تشيك على الـ `name` والـ `location` عشان أمنع دخول أي داتا فاضية أو مجرد مسافات (whitespaces) للـ database.

## Technical Details
- **UUIDs**: الـ IDs دلوقتي شغالة بـ **UUID** بدل الـ Integers التقليدية، وده أحسن للأمان والـ global uniqueness.
- **Endpoints**: كل الـ views شغالة بـ `@api_view` وبترجع الـ correct status codes والـ JSON responses بشكل بروفيشنال.

## Status
الـ tests كلها **passing** وزي الفل. الشغل جاهز تماماً للـ Friday review.

```powershell
# Run tests:
python manage.py test events
```
