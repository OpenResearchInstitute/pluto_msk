local binfin = ""
local open = io.open

local function read_file(path)
    local file = open(path, "rb") -- r read mode and b binary mode
    if not file then return nil end
    local content = file:read "*a" -- *a or *all reads the whole file
    file:close()
    return content
end

-- local fileContent = read_file("toto.txt");
-- print (fileContent);


function hex_dump(str)
    local len = string.len( str )
    local dump = ""
    local hex = ""
    local asc = ""
    
    for i = 1, len do
        if 1 == i % 8 then
            dump = dump .. hex .. asc .. "\n"
            hex = string.format( "%04x: ", i - 1 )
            asc = ""
        end
	        
        local ord = string.byte( str, i )
--        toBits(ord, 32)
	bin = table.concat(toBits(ord, 8))
        binfin = binfin .. bin
	hex = hex .. string.format( "%02x ", ord )
        if ord >= 32 and ord <= 126 then
            asc = asc .. string.char( ord )
        else
            asc = asc .. "."
        end
    end

    
    return dump .. hex
            .. string.rep( "   ", 8 - len % 8 ) .. asc
end

bits=8


function toBits(num, bits)
    -- returns a table of bits
    local t={} -- will contain the bits
    for b=bits,1,-1 do
        rest=math.fmod(num,2)
        t[b]=rest
        num=(num-rest)/2
    end
    if num==0 then return t else return {'Not enough bits to represent this number'}end
end

-- bits=toBits(num, bits)
-- print(table.concat(bits))
hex_dump(read_file("toto.txt"))
-- print(hex_dump(read_file("toto.txt")))
--print(hex_dump("rfghg"))
-- print(bin)
print(binfin)
-- print(table.concat(bits))
