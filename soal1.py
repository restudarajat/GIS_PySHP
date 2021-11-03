import shapefile
w=shapefile.Writer('soal1')
w.shapeType

w.field("upin1","C")
w.field("ipin2","C")

w.record("upin","satu")
w.record("ipin","dua")

w.point(1,1)
w.point(2,2)

