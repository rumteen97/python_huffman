from PIL import Image

# img = Image.open('image.png').convert('LA') #grayscale krdn e aks
# img.save('greyscale.png')
pic=Image.open('gray8bit.jpg')
pixel_list=list(pic.getdata()) #color codes

class NodeTree(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return "%s_%s" % (self.left, self.right)

def huffmanCodeTree(node, left=True, huffcode=""):
    if type(node) is int:
        return {node: huffcode}
    (l, r) = node.children()
    d = dict()
    d.update(huffmanCodeTree(l, True, huffcode + "0"))
    d.update(huffmanCodeTree(r, False, huffcode + "1"))
    return d

freq = {}
for c in pixel_list:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

nodes = freq

while len(nodes) > 1:
    key1, c1 = nodes[-1]
    key2, c2 = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))
    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffmanCode = huffmanCodeTree(nodes[0][0])

huffmansize=0
print " Color code | Freq  | Huffman code "
for colorcode, frequency in freq:
    print " %-10r | %5d | %15s" % (colorcode, frequency, huffmanCode[colorcode])
    huffmansize=huffmansize+(frequency*(len(huffmanCode[colorcode])))


freqsum=0
for z in pixel_list:
    freqsum=freqsum+8



print " \n actual size: ",freqsum,"bit"
print "\n huffman compression size: ",huffmansize,"bit"