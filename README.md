<h1>
  Factorio mod builder
</h1>

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
    - [example](#example-5)
  - [button](#button)
    - [description](#description-6)
    - [arguments](#arguments-3)
    - [example](#example-6)
  - [switch](#switch)
    - [description](#description-7)
    - [arguments](#arguments-4)
    - [example](#example-7)
  - [left](#left)
    - [description](#description-8)
  - [right](#right)
  - [slider](#slider)
    - [description](#description-9)
    - [arguments](#arguments-5)
    - [example](#example-8)
  - [textfield](#textfield)
  - [text-box](#text-box)
  - [locale](#locale)
  - [sprite](#sprite)
  - [vstack](#vstack)
  - [hstack](#hstack)
  - [vframe](#vframe)
  - [hframe](#hframe)

---

# Tags documentation
all the standard tags usable with context aware example

## gui

### description

the root element of all files in the folder `{mod}/fbuild/src/gui`

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

A piece of text

can be used in 2 ways:

- use directly with text
- use with a `<locale>` tag to use 
  [LocalizedString](https://lua-api.factorio.com/latest/Concepts.html#LocalisedString)

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
  localized text will show
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

---

## button

### description

A clickable Element

can be use in 3 ways:

- use directly with text
- use with the `<locale>` tag
- use with the `<sprite>` tag

### arguments

`mouse_button_filter` string?: Which mouse buttons the button responds to. Defaults to `"left-and-right"` see [MouseButtonFlags](https://lua-api.factorio.com/latest/Concepts.html#MouseButtonFlags)

`onClick` string: when the button is clicked it will call the function here specified

### example

```xml
<!--
  the button tag it self will show
  'Hello Button'
  in all languages

  when clicked will execute

  say_it_back()

-->
<gui>

  <body>
    <button onClick="say_it_back">
      Hello Button
    </button>
  </body>
</gui>

<!--
  localized text will show
  'Iron plate' in English
  or
  'Eisenplatte' in German
-->
<gui>

  <body>
    <button>
      <locale>
        item-name.iron-plate
      </locale>
    </button>
  </body>
</gui>

<gui>

  <body>
    <button>
      <sprite>
        item/iron-plate
      </sprite>
    </button>
  </body>
</gui>
```

---

## switch

### description

used with the tags `<left>` and `<right>` describes a switch 

### arguments

`switch_state` string?: Possible values are `"left"`, `"right"`, or `"none"`.
If set to `"none"`, allow_none_state must be `true`. Defaults to `"left"`

`allow_none_state` boolean?: Whether the switch can be set to a middle state.
Defaults to `false`

### example

```xml
<gui>

  <body>
    <switch allow_none_state="true" initial_value="none">

      <left>

        left label
        <tooltip>
          tooltip text
        </tooltip>

      </left>

      <right>

        <locale>
          locale.text
        </locale>

        <tooltip>
          <locale>
            tooltip.locale.text
          </locale>
        </tooltip>

      </right>

    </switch>
  </body>
</gui>
```

## left

### description

in the context of a switch describe the left label and can be used in 3 ways:

1. with direct text that will be used in thee label
2. with a `<locale>` that will translate the label in the current language
3. with a `<tooltip>` tag that will describe the hover tooltip

method `3` can be used together with method `1` or `2`

## right

same as [left](#left) but for the right side

## slider

### description

### arguments

`min_value` float?: The minimum value for the slider. Defaults to 0

`max_value` float?: The maximum value for the slider. Defaults to 30

`initial_value` float?: The initial value for the slider. Defaults to minimum_value

`step` float?: The minimum value the slider can move. Defaults to 1

### example

```xml
```

## textfield

## text-box

## locale

## sprite

## vstack

## hstack

## vframe

## hframe