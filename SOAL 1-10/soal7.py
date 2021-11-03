import shapefile
w=shapefile.Writer('./soal7', shapeType=shapefile.POLYLINE)
w.shapeType

w.field("upin1","C")
w.field("ipin2","C")

w.record("upin","satu")


w.line([[[1,3],[5,3],[1,2],[5,2]]])