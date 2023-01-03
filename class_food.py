class food:
    name='grocery'
    shelf_life=1
    package='box'
    def set (self,name, shelf_life, package,by_weight):
        self.name=name
        self.shelf_life=shelf_life
        self.package=package
class grocery(food):
    by_weight=1
groats=grocery()
shelf_life=12
package='box'
by_weight=1.000
groats.set ('groats', 12, 'box',1.000)
print(groats.name,shelf_life,package,by_weight)
pasta=grocery()
shelf_life=24
package='bundle'
by_weight=0.500
pasta.set('pasta',24,'bundle', 0.500)
print(pasta.name, shelf_life,package,by_weight)
class dairy_products(food):
    dairy_products=food()
    milk=dairy_products
    shelf_life=2
    package='box'
    by_weight=1.000
    milk.set('milk',2 ,'box', 1.000)
    print(milk.name,shelf_life,package,by_weight)







