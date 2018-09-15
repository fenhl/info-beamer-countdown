node.alias("countdown")

gl.setup(NATIVE_WIDTH, NATIVE_HEIGHT)

local text = require "text"

util.resource_loader{
    "dejavu_sans.ttf"
}

local write = text{font=dejavu_sans, width=WIDTH, height=HEIGHT, r=1, g=1, b=1}

local target_time = N.target_time or 0

util.data_mapper{
    ["delta/set"] = function(delta)
        target_time = sys.now() + tonumber(delta)
        N.target_time = target_time
    end;
}

function concat(arrays)
    local result = {}
    for i = 1, #arrays do
        for j = 1, #arrays[i] do
            result [#result + 1] = arrays[i][j]
        end
    end
    return result
end

--- a modified version of the countdown utility function from info-beamer-night. Modifications:
---
--- * does not prepend "in" to positive deltas
--- * expects the target time to be relative to the internal epoch based on sys.now() rather than the UNIX epoch
function countdown(target_time)
    -- determine remaining duration
    local delta = target_time - sys.now()
    -- format
    local past = false
    if delta < 0 then
        delta = -delta
        past = true
    end
    local result = {}
    local delta_minutes = delta / 60
    local delta_seconds = delta % 60
    local delta_hours = delta_minutes / 60
    delta_minutes = delta_minutes % 60
    local delta_days = delta_hours / 24
    delta_hours = delta_hours % 24
    if delta_days >= 1 then
        result = {
            string.format("%dd", delta_days),
            string.format("%02dh", delta_hours),
            string.format("%02dm", delta_minutes),
            string.format("%02ds", delta_seconds)
        }
    elseif delta_hours >= 1 then
        result = {
            string.format("%dh", delta_hours),
            string.format("%02dm", delta_minutes),
            string.format("%02ds", delta_seconds)
        }
    elseif delta_minutes >= 1 then
        result = {
            string.format("%dm", delta_minutes),
            string.format("%02ds", delta_seconds)
        }
    else
        result = {
            string.format("%ds", delta_seconds)
        }
    end
    if past then
        return concat{result, {"ago"}}
    else
        return result
    end
end

function node.render()
    gl.clear(0, 0, 0, 1)
    write{text={countdown(target_time)}}
end
