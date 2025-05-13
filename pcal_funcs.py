# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

def replace_last(source_string, replace_what, replace_with):
    if source_string.endswith(replace_what):
        return source_string[:-len(replace_what)] + replace_with
    return source_string


def cleanstr(s):
    s = s.strip()
    s = s.replace('ä', 'ae')
    s = s.replace('ö', 'oe')
    s = s.replace('ü', 'ue')
    s = s.replace('Ä', 'Ae')
    s = s.replace('Ö', 'Oe')
    s = s.replace('Ü', 'Ue')
    s = s.replace('ß', 'ss')
    s = s.replace(' ', '_')

    return s


def remove_pca_naming(s):
    s = replace_last(s, '_HANDLE', '')
    s = replace_last(s, '_EMPTY', '')
    s = replace_last(s, '_CAM', '')
    s = replace_last(s, '_DEPTH', '')
    s = replace_last(s, '_TOUR', '')
    return s
