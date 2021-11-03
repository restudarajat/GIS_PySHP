import shapefile

w=shapefile.Writer('soal5/soal5')
w.shapeType

w.field("upin1","C")
w.field("ipin2","C")

w.record("upin","satu")


w.line([[[1,5],[5,5],[5,1],[3,3],[1,1]]])
