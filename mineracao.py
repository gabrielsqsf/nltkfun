import nltk
import re
from nltk.corpus import gutenberg

def Jaccard(a,b):
    a_ = set(a)
    b_ = set(b)
    return 1-nltk.metrics.jaccard_distance(a_,b_)

def Demerau(a,b):
    a_ = a
    b_ = b
    return nltk.metrics.distance.edit_distance(a_,b_,True)

def n_window(string, number=3):
    l = list()
    for i in range(len(string)):
        l.append(string[i:i+number])
    return l

def similarity_gutenberg():
    for x in range(2,6):
        a = []
        b = 0
        c = 0
        d = 1

        for fid in gutenberg.fileids():
            a.append([])
            for ffid in gutenberg.fileids():
               a[b].append(Jaccard(n_window(gutenberg.raw(fid),x),n_window(gutenberg.raw(ffid),x)))
            b += 1

        for i in range(len(a)):
            for j in range(len(a)):
               c += a[i][j]/(len(a)*len(a))
               d = min(d,a[i][j])
        print("Media: "+ str(c))
        print("Minimo: "+ str(d))
    
def mean_len():
    a = []
    d = 1

    for fid in gutenberg.fileids():
        b = 0
        c = 0
        st = gutenberg.raw(fid)
        stl = re.split("\n|\.|\!|\?", st)
        stw = re.split("\n|\.|\!|\?| |,| - ", st)
        for el in stl:
            b += len(el)*(1.0)/len(stl)
        for el in stw:
            c += len(el)*(1.0)/len(stw)
        print(fid)
        print("Media Frases: "+ str(b))
        print("Media Palavras: "+ str(c))


text1 = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas elementum felis sed mi viverra, nec bibendum nulla luctus. Etiam vulputate diam eget tellus suscipit, in condimentum metus auctor. Curabitur nec egestas odio. Ut bibendum erat accumsan massa laoreet vulputate. Aenean posuere, lectus quis semper sagittis, magna magna volutpat enim, ac finibus turpis erat quis nulla. Vivamus semper mauris sit amet est suscipit, id mattis elit mollis. Sed non neque ut orci sagittis tincidunt at vitae nisi. Vivamus lacus sem, interdum eget ante nec, euismod consectetur urna.

Ut blandit tempus quam ut consectetur. Maecenas eleifend ut lacus vitae euismod. Nullam sodales dapibus metus a condimentum. Ut eget arcu at velit pellentesque imperdiet. Etiam id hendrerit neque, quis ultrices eros. Etiam hendrerit rutrum feugiat. Nulla volutpat nibh at luctus interdum. Sed mattis diam at eros placerat sollicitudin. Suspendisse ac sapien rutrum, aliquam elit non, tempor orci. In faucibus, enim sed malesuada eleifend, mi lorem eleifend augue, at lobortis lacus quam a lacus. Donec ultricies cursus quam et consectetur. Fusce vitae augue tincidunt, bibendum orci ac, interdum ante. Fusce elementum eros a enim pharetra, et volutpat metus vulputate. Aliquam tristique dolor ac bibendum euismod. Curabitur at efficitur purus, sed aliquet nisi. Nam a massa non ipsum malesuada gravida.

Curabitur felis mi, pretium pulvinar magna quis, fermentum varius diam. Pellentesque ultrices imperdiet nisi, sit amet imperdiet neque ultricies vel. Mauris facilisis erat condimentum risus viverra, a rhoncus quam maximus. Curabitur a sem consequat, pulvinar sem ut, mollis eros. Duis lacinia mauris sed nulla cursus, non dapibus lorem rhoncus. Quisque at viverra neque. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Phasellus in quam iaculis quam elementum fringilla. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vivamus suscipit ligula ac accumsan sollicitudin. Proin eleifend massa diam, id tincidunt tellus feugiat vel. Nunc dictum neque eleifend, aliquet nulla quis, lacinia purus. Donec vel accumsan nunc.

Vestibulum risus erat, viverra ut ante nec, finibus posuere augue. Aenean tempus dolor non felis viverra elementum nec a diam. Duis ultrices ante risus, vitae condimentum leo ultrices sit amet. Curabitur quis ipsum mauris. Sed augue magna, finibus vel tellus quis, lobortis luctus metus. Phasellus id lectus ac erat pharetra molestie id at arcu. Phasellus tristique orci vel elit euismod, ut gravida velit accumsan. In a porta ante, eget fringilla dolor. Ut efficitur enim vitae nisi rhoncus, a feugiat eros consequat. Mauris feugiat elit nec lorem viverra, in luctus tortor viverra. Cras egestas lacinia diam id vestibulum. Praesent imperdiet ipsum id arcu fringilla molestie. Pellentesque ut justo eu nunc bibendum condimentum eget et leo. Curabitur euismod ipsum odio, at convallis sapien aliquam ac. Morbi aliquet tincidunt aliquam.

Maecenas luctus neque blandit dui semper elementum. Suspendisse viverra ligula ante, eget elementum ex egestas mollis. Curabitur egestas bibendum elit vitae euismod. Vivamus ullamcorper laoreet tellus at laoreet. Sed auctor metus quis nisl luctus, eu maximus sem venenatis. Ut eleifend nisi nisi, ut scelerisque justo commodo nec. Sed quis massa ultrices, varius lorem cursus, pretium nisi. Suspendisse consequat purus massa, vel condimentum sapien volutpat imperdiet. Aenean pellentesque, elit et facilisis eleifend, nunc nibh porttitor orci, sit amet volutpat metus mi in ipsum. Phasellus a blandit dolor. Morbi condimentum libero et luctus iaculis. Donec ultricies fringilla mattis. Aenean sit amet consequat purus. Duis ipsum felis, tempor eget lobortis nec, facilisis a turpis. Vestibulum venenatis ullamcorper eros, vel volutpat nisl ullamcorper non."""

text2 = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus consectetur scelerisque dolor, ac condimentum augue egestas sed. Donec at mattis arcu. Cras suscipit erat velit, sagittis consequat ex bibendum id. Donec molestie odio eu nisi elementum, vel ultricies dui scelerisque. Nam et metus in libero tristique dictum. Cras convallis scelerisque dolor vitae finibus. Nunc id porttitor odio, eu luctus lectus. Fusce metus nibh, tempor eget libero vitae, placerat venenatis diam.

Integer non semper eros. Curabitur id leo nec orci elementum imperdiet. Mauris magna arcu, vestibulum in sem eu, volutpat volutpat mauris. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Sed fringilla vulputate orci, id cursus enim facilisis ut. Duis quis enim diam. Proin eleifend velit diam, vel mollis justo tristique eget. Nulla lobortis risus justo, id egestas eros auctor eget.

Nulla eu quam magna. Nulla lacinia pellentesque leo vitae consequat. Etiam quis gravida nunc. Vivamus ac sapien posuere, dictum nisi ac, euismod felis. Nulla porttitor ullamcorper sapien, sit amet sodales tortor porttitor in. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nunc sed tellus non neque posuere lobortis et dignissim lectus.

Donec sit amet molestie tortor, sed porttitor diam. Vestibulum sed aliquam urna. Etiam pharetra blandit hendrerit. In condimentum risus ut magna rutrum, quis fringilla felis tincidunt. Sed dictum erat pulvinar metus ornare ullamcorper. Quisque efficitur sapien vel dui consectetur vestibulum. Proin facilisis enim leo, a condimentum justo dapibus eget. Maecenas tempor nunc eget tempor fringilla. Vivamus venenatis, orci quis eleifend lacinia, augue tortor varius neque, vel luctus arcu massa vel eros. Nunc libero tortor, molestie id nisi vel, auctor dapibus diam. Sed egestas non magna ac feugiat. Proin ligula metus, gravida at semper non, lobortis vitae nisi.

Sed fermentum malesuada luctus. Etiam a sem non nisl congue lobortis. Quisque dapibus semper nibh non cursus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Cras convallis, velit vel mollis hendrerit, libero nisi venenatis sem, sed tempus purus orci non eros. Sed non risus eros. Suspendisse vehicula ut leo ultrices efficitur. Maecenas a maximus neque, et ullamcorper mi."""

