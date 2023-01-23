<h1> Factorio mod builder fbuild </h1>

# Table of Content
- [Table of Content](#table-of-content)
- [Tags documentation](#tags-documentation)
  - [gui](#gui)
    - [description](#description)
    - [arguments](#arguments)
    - [example](#example)
  - [component](#component)
    - [description](#description-1)
    - [arguments](#arguments-1)
    - [example](#example-1)
  - [head](#head)
    - [description](#description-2)
    - [example](#example-2)
  - [body](#body)
    - [description](#description-3)
    - [example](#example-3)
  - [include](#include)
    - [description](#description-4)
    - [arguments](#arguments-2)
    - [example](#example-4)
  - [label](#label)
    - [description](#description-5)
    - [args](#args)
    - [example](#example-5)
  - [button](#button)
  - [switch](#switch)
  - [slider](#slider)
  - [textfield](#textfield)
  - [text-box](#text-box)
  - [locale](#locale)
  - [sprite](#sprite)

---

# Tags documentation
all the standard tags usable with context aware example

## gui

### description

the root element of all files in the folder `{mod}/mb/src/gui/roots`

### arguments

`name` string: the name of the gui 

### example

```xml

<gui name="gui-name">

</gui>

```

---

## component

### description

the root element of all components used to create macros

### arguments

`name` string: the name of the component used in the xml tags 

### example

```xml

<component name="example-component">

</component>

```

---

## head

### description

inside this tag is all data used to setup the gui

### example

```xml
<gui>
    <head>

    </head>
</gui>
```

---

## body

### description

inside this tag is the tag used to render the gui

### example

```xml
<gui>
    <body>

    </body>
</gui>
```

---

## include

### description

the content of this tag is where are the file/s to include

### arguments

`type` string: describees what type of file is pointed to can be: `style`, `component`

### example

```xml
<gui>
    <head>
        <include type="style">styles/common.fstyle</include>
        <include type="component">components/supertable.xml</include>
    </head>
</gui>

```

---

## label

### description

can be used in 2 ways:

- use directly with text
- use with a `<locale>` tag to use 
  [LocalizedString](https://lua-api.factorio.com/latest/Concepts.html#LocalisedString)

### args

### example

```xml
<!--
  this will show
  'normal text here'
  in all languages
  -->
<gui>

  <body>
    <label>
      normal text here
    </label>
  </body>
</gui>

<!--
  localized text
  will show
  'Iron plate' in English
  or
  'Eisenplatte' in German
-->
<gui>

  <body>
    <label>
      <locale>
        item-name.iron-plate
      </locale>
    </label>
  </body>
</gui>
```

## button

## switch

## slider

## textfield

## text-box

## locale

## sprite