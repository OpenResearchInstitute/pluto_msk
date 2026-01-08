set project_name [lindex $argv 0]
if { $project_name eq "" } {
    set project_name "e310"
}

puts "Generating FSBL for project: $project_name"
hsi open_hw_design $project_name.sdk/system_top.xsa
set cpu_name [lindex [hsi get_cells -filter {IP_TYPE==PROCESSOR}] 0]

setws ./build/sdk
app create -name fsbl -hw $project_name.sdk/system_top.xsa -proc $cpu_name -os standalone -lang C -template {Zynq FSBL}
app config -name fsbl -set build-config release
app build -name fsbl
