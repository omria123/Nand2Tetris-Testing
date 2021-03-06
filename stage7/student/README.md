
מאחר ולכתוב באסמבלי כמו שבטח כבר שמתם לב, זה לא כל כך כיף, אנחנו צריכים לעלות ברמה.
אנחנו רוצים לכתוב בשפה נוחה שיכולה לתת לנו להשתמש במשתנים באופן נורמלי, ולא לנהל זיכרון באופן כפייתי.


לשם כך אתם תכתבו קומפיילר לשפת התכנות Jack - שפה מונפצת לצרכי למידה, מזכירה את Java.

על מנת לכתוב את הקומפיילר אנחנו נבין תחילה תהליך הקימפול עובד. לשם כך תמיד טוב להתחיל בהיסטוריה -
אחרי ששמו לב שלכתוב באסמבלי זה פשוט סיוט, אנשים הבינו כי אפשר לוותר על זה אם הם יכתבו משהו שיתרגם
עבורם שפה קצת יותר אנושית. - כך נולדו שפות התכנות הראשונות שאינן שפות מכונה, הראשונה שבהן היא Fortran.
יותר מאוחר, מאחר והיה אפשר להתחיל לכתוב קצת יותר בחופשיות, התקדמנו לשפות נוחות יותר 
למשתמש  C,C++ ועוד רבות. ככל שהשפה היתה נוחה יותר למשתמש לרוב גם הקומפיילר נדרש לבצע יותר עבודה, 
מאחר והתרחק משפת המכונה.

בנקודה זו המתכנתים נתקלו בבעיה, חוץ משפות תכנות שהמשיכו להופיע, ישנם גם יצרני מעבדים חדשים בשוק,
שיוצרים עוד ועוד סוגי מעבדים, שכל אחד מביא את שפת המכונה שלו (ARM, x86, MIPS...). לכן המתכנתים נדרשו 
לייצר קומפיילר פר (שפת מכונה, שפת תכנות) מה שיצר צורך בכתיבה n*m קומפיילרים עבור n שפות מכונה, m
שפות תכנות. בשביל זה המציאו שפת ביניים, שפה מומצאת שהיא בין שפת מכונה לשפת תכנות.
כאשר יהיה יחסית קל לממש את פעולות המכונה מעל שפות מכונה, וקל לממש קומפיילרים לאותן שפות.
מכך נקבל שעבור n, m עלינו ליצור n+m קומפיילרים קלים יותר לכתיבה.

בשני הפרקים הקרובים תממשו את השלב שפת מכונה וירטואלית -> שפת מכונת HACK.
בפרק שאחריהם תממשו תוכנית קטנה בשפת Jack על מנת להכיר את השפה אותה תקמפלו.
בשני הפרקים שאחריו תממשו את השלב שפת תכנות -> מכונה וירטואלית ובכך תשלימו את הקומפיילר הראשון שלכם!


כעת נתמקד בשפת המכונה הוירטואלית:
שפת המכונה עובדת עם stack. היא יכולה לדחוף למחסנית איברים ולבצע עליהם פעולות.
לשפה פקודות אריתמטיות: add, sub.
פקודות השוואתיות: eq, gt, lt.
פקודות בינאריות: and, or, not.
הפקודות פועלות על האיברים שבראש המחסנית, הן מוציאות אותם מהמחסנית מבצעות את הפעולה המתאימה ומחזירות את התוצאה.

גישות לזיכרון: על מנת לגשת לכתובות בזיכרון, המכונה מגדירה סגמנטים בזיכרון. היא נותנת גישה לאינדקסים
מתוך הסגמנטים השונים. (סגמנט לדוגמא static). הגישה מתבצעת באמצעות פעולות המחסנית:
למשל אם x המשתנה הראשון הסטטי וy השני בתחום הלוקאלי, אז בשפת התכנות הפעולה y=x מתורגם ל:
push static 0 
pop local 1
במצגת המצורפת מתואר כיצד ניתן לממש את הגישות לסגמנטים השונים באסמבלי.

בפרק הקרוב תממשו את פקודות שפת המכונה המצוינות כאן. עליכם לבנות מתרגם בפייתון 3 בשם translator.py שיודע להמיר תוכנה
בקובץ .vm לתוכנה מתאימה בקובץ .asm. על מנת לבדוק את עצמכם קיבלתם מספר תוכנות שעליכם לתרגם כהלכה:
פעולות אריתמטיות: (מומלץ תחילה לממש רק את פקודות אילו ואז להמשיך הלאה).
SimpleAdd.vm
StackTest.vm
פעולות בזיכרון:
BasicTest.vm
PointerTest.vm
StackTest.vm


טיפים:
1. יש לכם בנוסף לקבצי ה.tst הרגילים שיבחנו את תוצרי ה .asm שלכם, יש גם קבצי VME.tst מתאימים.הם נועדו
לתת לכם להריץ את הקוד שיש בתוך קובץ ה.vm כדי שתוכלו להבין מה מטרת התוכנית אותה אתם מתרגמים.
2. בקוד של המתרגם של השלב הנוכחי תרצו להשתמש גם לשלב הבא, מומלץ לכתוב את המתרגם באופן שיהיה
נוח להרחיב אותו בהמשך.
3. כלל הפקודות בVM ניתנות לתרגום פקודה פקודה - כלומר ניתן לתרגם כל פקודה ללא כל תלות בשאר הפקודות.

פקודה לדוגמא:
python3 trasnlator.py XXX.vm
# Generates XXX.asm.  
עליכם להגיש לבסוף את translator.py



#################################################
החלק הבא מיועד לשלב הבא במערך.

בפרק שלאחר מכן תממשו control flow commands:
label, goto, if-goto - המאפשרות קפיצות בקוד ותנאים.
לאחר מכן תממשו פונקציות בתוך השפה:
function <name> numOfLocalVars
call <name> numOfFuncArgs
return 

על מנת להריץ פונקציה במכונה הוירטואלית יש לקרוא לדחוף תחילה את המשתנים, ואז לקרוא לה בעזרת call כאשר מציינים את מספר הארגומנטים שהוכנסו.

כאן הסגמנטים נכנסים לפעולה, למעשה הסגמנטים ממומשים על ידי מצביעים השמורים בזיכרון המצביעים לתחילת
הסגמנט, כל פונקציה צריכה למשל סגמנט ארגמונטים שמצביע למיקום הארגומנט הראשון ב stack.
בנוסף כל פונקציה גם צריכה משתנים לוקאליים, כתובת אליה היא תחזור בסוף ריצת הפונקציה (כלומר המקום ממנו
קראו לפונקציה) ועוד. כל זאת ישמר במה שנקרא stack frame. כלומר בעת קריאה לפונקציה אחרת נדחוף את 
כל אלה למחסנית (כדי שכשנחזור מהפונקציה נוכל לשחזר הכל) ונגדיר מחדש את הסגמנטים בהתאם לקונטקסט
של הפונקציה החדשה (נקצה לה משתנים לוקאליים, וכו).

-- צורך בפיצר נוסף: אם המתרגם מקבל תיקייה במקום קובץ .vm עליו לתרגם את כלל קבצי ה .vm שבתוכם
לתוך קובץ .asm אחד באותו שם של התיקייה. בדומה לקומפיילר שיכול לקבל מספר קבצי .c ולתרגם אותם לקובץ ELF/exe יחיד.

הסבר מפורט יינתן במצגת המצורפת בשלב הבא.
לפרק הבא תצטרכו להגיש את המתרגם לאחר שהוא יודע לתרגם את:
קפיצות ותנאים:
BasicLoop.vm
FibonacciSeries.vm
פונקציות:
SimpleFunction.vm
(directory) NestedCall:
	Main.vm	
	Sys.vm

(directory) FibonacciElement:
	Main.vm
	Sys.vim


(directory) StaticsTest: 
	Class1.vm 
	Class2.vm 
	Sys.vm

טיפים:
1. התרגיל nestedcall הוא מעין שלב ביניים בין simpleFunction.vm לבין Fibonacci
2. על כל תיקייה להיות מתורגמת כ:
python translator.py <dirname>

הגישו שוב את translator.py, אחרי שהצלחתם לגרום לו לעבוד עם הקבצים לעיל
