<?xml version="1.0" encoding="UTF-8"?>
<!-- generated by wxGlade 0.9.9pre on Thu Oct 31 20:46:09 2019 -->

<resource version="2.3.0.1">
    <object class="wxFrame" name="frameMainCnrtl">
        <size>750, 550</size>
        <style>wxDEFAULT_FRAME_STYLE|wxFULL_REPAINT_ON_RESIZE</style>
        <title>Props Servo Control</title>
        <object class="wxToolBar" name="frameMainCnrtl_toolbar">
        </object>
        <object class="wxBoxSizer">
            <orient>wxVERTICAL</orient>
            <object class="sizeritem">
                <option>1</option>
                <flag>wxEXPAND</flag>
                <object class="wxBoxSizer">
                    <orient>wxHORIZONTAL</orient>
                    <object class="sizeritem">
                        <option>1</option>
                        <object class="wxGridSizer">
                            <cols>3</cols>
                            <hgap>0</hgap>
                            <rows>3</rows>
                            <vgap>0</vgap>
                            <object class="sizeritem">
                                <object class="wxButton" name="btnMoveServo">
                                    <label>Move Servo</label>
                                </object>
                            </object>
                            <object class="sizeritem">
                                <object class="wxTextCtrl" name="txtPosition">
                                </object>
                            </object>
                            <object class="spacer">
                                <size>0, 0</size>
                            </object>
                            <object class="spacer">
                                <size>0, 0</size>
                            </object>
                            <object class="spacer">
                                <size>0, 0</size>
                            </object>
                            <object class="spacer">
                                <size>0, 0</size>
                            </object>
                            <object class="spacer">
                                <size>0, 0</size>
                            </object>
                            <object class="spacer">
                                <size>0, 0</size>
                            </object>
                            <object class="spacer">
                                <size>0, 0</size>
                            </object>
                        </object>
                    </object>
                    <object class="spacer">
                        <size>0, 0</size>
                    </object>
                </object>
            </object>
            <object class="spacer">
                <size>0, 0</size>
            </object>
            <object class="sizeritem">
                <flag>wxEXPAND</flag>
                <object class="wxTextCtrl" name="statusTextBox">
                    <size>700, 200</size>
                    <style>wxHSCROLL|wxTE_MULTILINE|wxTE_READONLY</style>
                </object>
            </object>
            <object class="sizeritem">
                <object class="wxTextCtrl" name="txtSpeed">
                </object>
            </object>
        </object>
    </object>
</resource>