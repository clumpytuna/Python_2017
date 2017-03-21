import argparse
from sys import stdin, stdout


def split_into_paragraphs(lines):

    current_paragraph = []
    paragraphs = []

    for line in lines:
        if line == '' and current_paragraph == []:
            continue
        else:
            if line == '':
                paragraphs.append(''.join(current_paragraph))
                current_paragraph = []
            else:
                current_paragraph.append(line)
                current_paragraph.append(' ')

    if current_paragraph:
        paragraphs.append(''.join(current_paragraph))

    return paragraphs


def is_word_correct(word, line_length):
    if len(word) > line_length:
        print("Length of word > maximum line length")
        exit(1)


def split_into_words(paragraph, line_length):
    punctuation_marks = {',', '.', '?', '!', '-', ':', '\’'}
    words = []
    current_word = []
    new_word = False
    for each in paragraph:
            if each != ' ':
                if each in punctuation_marks:
                    current_word.append(each)
                else:
                    if new_word:
                        word = ''.join(current_word)
                        is_word_correct(word, line_length)
                        words.append(word)
                        current_word = [each]
                        new_word = False
                    else:
                        current_word.append(each)
            else:
                if current_word:
                    new_word = True
                else:
                    continue
    if current_word:
        word = ''.join(current_word)
        is_word_correct(word, line_length)
        words.append(word)
    return words


def paragraph_builder(words, line_length, num_spaces):
    paragraph = [' ']
    words[0] = ' ' * num_spaces + words[0]
    is_word_correct(words[0], line_length)
    current_line = ''
    for word in words:
        if len(current_line) + len(word) <= line_length:
            current_line += word + ' '
        else:
            paragraph.append(current_line.rstrip(' ') + '\n')
            current_line = ''
    if current_line:
        paragraph.append(current_line.rstrip(' ') + '\n')
    return ''.join(paragraph)


def text_printer(paragraphs, line_length, num_spaces, output_):
    if output_ != stdout:
        output_file = open(output_.name, 'w')
        for paragraph in paragraphs:
            output_file.write(paragraph_builder(split_into_words(paragraph, line_length),
                                                line_length, num_spaces))
            output_file.write('\n')
    else:
        output_.write('\n')
        for paragraph in paragraphs:
            output_.write(paragraph_builder(split_into_words(paragraph, line_length),
                                            line_length, num_spaces))
        output_.write('\n')


def formatter_(input_, output_, line_length, num_spaces):
    lines = input_.read().split('\n')
    text_printer(split_into_paragraphs(lines),
                 line_length, num_spaces, output_)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=argparse.FileType('r'), default=stdin)
    parser.add_argument('-o', '--output', type=argparse.FileType('w'), default=stdout)
    parser.add_argument('-l', '--line-length', type=int, required=True)
    parser.add_argument('-p', '--paragraph-spaces', type=int, required=True)
    args = parser.parse_args()
    formatter_(args.input, args.output, args.line_length, args.paragraph_spaces)

if __name__ == "__main__":
    main()
