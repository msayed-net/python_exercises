# This is a program that can calculate students degrees
Id_dict = dict({'Ali' : 0, 'Ahmed' : 0, 'Mohamed' : 0})

midterm_ali = float(input('Midterm - Ali : '))
midterm_ahmed = float(input('Midterm - Ahmed : '))
midterm_mohamed = float(input('Midterm - Mohamed : '))

Id_dict['Ali'] += midterm_ali
Id_dict['Ahmed'] += midterm_ali
Id_dict['Mohamed'] += midterm_ali

sketch_ali = float(input('Sketch - Ali : '))
sketch_ahmed = float(input('Sketch - Ahmed : '))
sketch_mohamed = float(input('Sketch - Mohamed : '))

Id_dict['Ali'] += sketch_ali
Id_dict['Ahmed'] += sketch_ahmed
Id_dict['Mohamed'] += sketch_mohamed

final_ali = float(input('final - Ali : '))
final_ahmed = float(input('final - Ahmed : '))
final_mohamed = float(input('final - Mohamed : '))

Id_dict['Ali'] += final_ali
Id_dict['Ahmed'] += final_ahmed
Id_dict['Mohamed'] += final_mohamed

print("Ali degree is, {0}".format(Id_dict.get('Ali')))
print("Ahmed degree is, {0}".format(Id_dict.get('Ahmed')))
print("Mohamed degree is, {0}".format(Id_dict.get('Mohamed')))
