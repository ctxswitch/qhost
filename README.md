# qhost
[![Build Status](https://travis-ci.org/rlyon/qhost.svg?branch=master)](https://travis-ci.org/rlyon/qhost)

Gridengine qhost replacement for PBS based systems. Summarize pbsnodes output in a quick list. View execution node information such as processors, running jobs, memory stats, and state.

## Current Version
1.3.1

## Changes
There are several significant changes in output and functionality in 1.2.x and 1.3.x.  The state is now displayed as an offset character representing the 8 possible PBS states.  This was done for two reasons: 1) make the output easier to scan, and 2) keep the lines a static length when multiple states were present (i.e. job-exclusive and down/offline).  

The other significant change is the addition of filters.  Using the ```state``` or ```s``` option, you can pass in the same characters used to represent state in the output to filter and display the nodes in the specified states.  The default is to display all states.  The ```jobid``` or ```j``` options can be used to filter based on a specific job id.  For the final argument you can provide a regular expression for node name matching.  The expression will match any part of the node unless you specify the beginning and end of the pattern (i.e. "^n.*4$") Some examples are:

```sh
$ qhost n0[15]
NODE               OS      CPU GPU MEMTOT   MEMUSE   JOBS SLOT LOAD    STATE
--------------------------------------------------------------------------------
n010               linux   8   0   33.4G    1.9G     0    0    0.0    | F
n011               linux   8   0   33.4G    1.9G     0    0    0.0    | F
n012               linux   8   0   33.4G    1.9G     0    0    0.02   | F
n013               linux   8   0   33.4G    1.9G     0    0    0.01   | F
n014               linux   8   0   33.4G    1.1G     0    0    0.0    |  O
n015               linux   8   0   33.4G    2.0G     0    0    0.0    | F
n016               linux   8   0   33.4G    2.0G     0    0    0.14   | F
n017               linux   8   0   33.4G    1.7G     0    0    0.0    | F
n018               linux   8   0   33.4G    2.0G     0    0    0.0    | F
n019               linux   8   0   33.4G    1.9G     0    0    0.0    | F
n050               linux   8   0   33.4G    2.6G     0    0    0.03   | F
n051               linux   8   0   33.4G    2.6G     0    0    0.0    | F
n052               linux   8   0   33.4G    2.5G     0    0    0.0    | F
n053               linux   8   0   33.4G    1.5G     0    0    0.03   | F
n054               linux   8   0   33.4G    2.6G     0    0    0.0    | F
n055               linux   8   0   33.4G    2.6G     0    0    0.0    | F
n056               linux   8   0   33.4G    1.6G     0    0    0.0    | F
n057               linux   8   0   33.4G    1.6G     1    8    8.25   |     E
n058               linux   8   0   33.4G    3.1G     1    8    8.02   |     E
n059               linux   8   0   33.4G    2.5G     1    8    8.0    |     E
$ qhost -s OE n0[15]
NODE               OS      CPU GPU MEMTOT   MEMUSE   JOBS SLOT LOAD    STATE
--------------------------------------------------------------------------------
n014               linux   8   0   33.4G    1.1G     0    0    0.0    |  O
n057               linux   8   0   33.4G    1.6G     1    8    8.25   |     E
n058               linux   8   0   33.4G    3.1G     1    8    8.02   |     E
n059               linux   8   0   33.4G    2.5G     1    8    8.0    |     E
$ qhost "^n.*4$"
NODE               OS      CPU GPU MEMTOT   MEMUSE   JOBS SLOT LOAD    STATE
--------------------------------------------------------------------------------
n004               linux   8   0   33.4G    1.9G     0    0    0.07   | F
n014               linux   8   0   33.4G    1.1G     0    0    0.0    |  O
n024               linux   8   0   33.4G    2.0G     0    0    0.04   | F
n034               linux   8   0   33.4G    2.0G     0    0    0.04   | F
n044               linux   8   0   33.4G    2.1G     0    0    0.0    | F
n054               linux   8   0   33.4G    2.6G     0    0    0.0    | F
n064               linux   8   0   33.4G    22.7G    1    1    1.0    | F
$ qhost -j -J 1158770
NODE               OS      CPU GPU MEMTOT   MEMUSE   JOBS SLOT LOAD    STATE
--------------------------------------------------------------------------------
n057               linux   8   0   33.4G    1.6G     1    8    8.25   |     E
                   Jobs        : 1158770
n058               linux   8   0   33.4G    3.1G     1    8    8.02   |     E
                   Jobs        : 1158770
n059               linux   8   0   33.4G    2.5G     1    8    8.0    |     E
                   Jobs        : 1158770
n060               linux   8   0   33.4G    1.9G     1    8    8.08   |     E
                   Jobs        : 1158770
```

## Install

Clone this repository then:

    # git clone https://github.com/rlyon/qhost
    # cd qhost
    # python setup.py install

## Usage

qhost \[options\] \[optional-node-regex\]

### Options

* ```-c, --color``` - colorize some of the output
* ```-j, --jobs``` - display job information with the node
* ```-p, --properties``` - display the node properties
* ```-n, --ntype``` - display the node type
* ```-a, --all``` - display all extended attributes including jobs, ntype and properties
* ```-s STATE, --state=STATE``` - Filter nodes by state. Valid state characters are F (free), O (offline), D (down), R (reserve), E (job-exclusive), S (job-sharing), B (busy), T (time-shared), and U (state-unknown).
* ```-J JOBID, --jobid=JOBID``` - Filter nodes by jobid.
* ```-X XMLFILE, --xmlfile XMLFILE``` - use a previously stored xml file instead of calling pbsnodes
* ```-v, --version``` - display the version and exit
* ```-h, --help``` - display the help and exit

## Contributing

### Grab the source and make a branch

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Make your changes
4. Add some tests
5. Commit your changes (`git commit -am 'Add some feature'`)
6. Push to the branch (`git push origin my-new-feature`)
7. Create new Pull Request

### Reporting/Fixing bugs

If you run into an issue, save the output of ```pbsnodes -x``` so the issue can be isolated and tests created.  If you use the output for a test, please make sure you de-identify anything that you don't want available for the world to see.
