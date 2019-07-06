# INI Parser
## `namespace INIParser`
### `static class IniFile`
Creator for INI objects in the assembly.
#### `static INIReader CreateReader(string path)`
Create an INI reader.
#### `static INIWriter CreateWriter(string path)`
Create an INI writer.
### `interface INIReader`
Represents an INI reader.
#### `string Read(string Key, string Section)`
Reads a value in the INI.
### `interface INIWriter`
Represents an INI writer.
#### `void Write(string Key, string Value, string Section = null)`
Write a value to an INI file.
#### `void DeleteKey(string Key, string Section = null)`
Deletes a key in an INI file.
#### `void DeleteSection(string Section = null)`
Deletes a section in an INI file.
