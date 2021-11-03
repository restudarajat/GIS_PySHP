import shapefile
w=shapefile.Writer('./soal8', shapeType=shapefile.POLYGON)
w.shapeType

w.field("upin1","C")
w.field("ipin2","C")

w.record("upin","satu")


w.poly([[[1,3],[5,3],[1,2],[5,2], [1,3]]])