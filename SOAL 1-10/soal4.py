import shapefile

w=shapefile.Writer('soal4' , shapefile.POINTM)
w.shapeType

w.field("upin1","C")
w.field("ipin2","C")

w.record("upin","satu")
w.record("ipin","dua")

w.pointm(1,1)
w.pointm(2,2)

w.close()