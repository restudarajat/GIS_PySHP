import shapefile

w = shapefile.Writer('soal9')
w.shapeType

w.field("upin1","C")
w.field("ipin2","C")

w.record("tes1","satu")
w.record("tes2","dua")


w.poly([[
    [1,3],
    [5,3],
    [5,2],
    [1,2],
    [1,3]
]])

w.poly([[
    [1,6],
    [5,6],
    [5,9],
    [1,9],
    [1,6]
]])


w.close()