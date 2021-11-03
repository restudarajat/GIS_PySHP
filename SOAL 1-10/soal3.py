import shapefile

w=shapefile.Writer('soal3', shapeType=1)
w.shapeType
w.shapeType=3
w.shapeType

w.field("upin1","C")
w.field("ipin2","C")

w.record("upin","satu")

w.line([[[1,1],[2,2]]])