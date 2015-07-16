# Machines for [![][machinehub-logo]](https://github.com/bq/machinehub)

## Machine template

### Document

#### Title

```bash
-title-
Awesome Machine
```

#### Description

```bash
-description-
Does awesome stuff
```

#### Images

```bash
-images_url-
http:/web/path/to/image/1.png
http:/web/path/to/image/2.jpg
```

### Input parameters

#### Integer

```bash
int(a)
int(a=10)
int(a,(0:5:100))
int(a=10,(0:5:100))
int(a,[10,20,30])
int(a=20,[10,20,30])
```

#### Float

```bash
float(a)
float(a=3.14)
float(a,(0:0.1:1))
float(a=0.5,(0:0.1:1))
float(a,[0.9,1.0,1.1])
float(a=1.1,[0.9,1.0,1.1])
```

#### String

```bash
str(a)
str(a='default')
str(a,['cats','dogs'])
str(a='dogs',['cats','dogs'])
```

### Null example

File null-example.py

```bash

def machinebuilder(number, text):
    '''
[doc]
-title-
Null Machine
-description-
Does nothing
[inputs]
int(number,[10,20,30])
str(text='default')
    '''

    ###### Insert code here ######

    # return result file name
    return ''
```

[machinehub-logo]: docs/img/machinehub.png
