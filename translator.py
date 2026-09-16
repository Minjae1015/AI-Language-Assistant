import java.util.Scanner;
import java.util.ArrayList;
import java.io.File;
import java.io.FileWriter;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;

public class Translator {

    // 사용할 언어

    static String[] languages = {
        "한국어",
        "영어",
        "일본어",
        "중국어(간체)",
        "프랑스어",
        "독일어",
        "스페인어",
        "자동 감지"
    };

    static String[] lang_codes = {
        "ko",
        "en",
        "ja",
        "zh-CN",
        "fr",
        "de",
        "es",
        "auto"
    };

    // 기록 저장

    static ArrayList<String> history = new ArrayList<>();
    static String history_file = "history.txt";

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        while (true) {

            System.out.println(" \n \n AI Language Assistant");
            System.out.println("[1] 번역하기");
            System.out.println("[2] 번역 기록");
            System.out.println("[3] 저장된 기록");
            System.out.println("[4] 기록 삭제");
            System.out.println("[5] 종료");

            String first_menu = scanner.nextLine();

            if (first_menu.equals("2")) {

                System.out.println(" \n \n 번역 기록입니다:");

                if (history.size() == 0) {
                    System.out.println("기록이 없습니다.");
                }

                else {
                    int count = 1;

                    for (String record : history) {
                        System.out.println("\n[" + count + "]");
                        System.out.println(record);
                        count++;
                    }
                }

                System.out.println(" \n \n 엔터를 누르면 메뉴로 돌아갑니다");
                scanner.nextLine();
                continue;
            }

            else if (first_menu.equals("3")) {

                File file = new File(history_file);

                if (file.exists()) {

                    System.out.println(" \n \n 저장된 기록입니다:\n");

                    try {
                        BufferedReader reader = new BufferedReader(
                            new FileReader(history_file)
                        );

                        String line;

                        while ((line = reader.readLine()) != null) {
                            System.out.println(line);
                        }

                        reader.close();

                    } catch (IOException e) {
                        System.out.println("오류가 발생했습니다");
                    }

                }

                else {
                    System.out.println("저장된 기록이 없습니다");
                }

                System.out.println(" \n \n 엔터를 누르면 메뉴로 돌아갑니다");
                scanner.nextLine();
                continue;
            }

            else if (first_menu.equals("4")) {

                File file = new File(history_file);

                if (!file.exists()) {
                    System.out.println("삭제할 기록이 없습니다");
                    System.out.println(" \n \n 엔터를 누르면 메뉴로 돌아갑니다");
                    scanner.nextLine();
                    continue;
                }

                System.out.println(" \n \n 정말 기록을 삭제하시겠습니까?");
                System.out.println("[1] 예");
                System.out.println("[2] 아니오");

                String delete_choice = scanner.nextLine();

                if (delete_choice.equals("1")) {

                    file.delete();
                    history.clear();

                    System.out.println("번역 기록이 삭제되었습니다");
                }

                else if (delete_choice.equals("2")) {
                    System.out.println("삭제를 취소했습니다");
                }

                else {
                    System.out.println("다시 입력해주세요");
                }

                System.out.println(" \n \n 엔터를 누르면 메뉴로 돌아갑니다");
                scanner.nextLine();
                continue;
            }

            else if (first_menu.equals("5")) {
                System.out.println("프로그램 종료");
                break;
            }

            else if (!first_menu.equals("1")) {
                System.out.println("다시 입력해주세요");
                continue;
            }

            // 원본 언어

            int source_choice;

            while (true) {

                System.out.println(" \n \n 원본 언어를 선택하세요");

                for (int i = 0; i < languages.length; i++) {
                    System.out.println("[" + (i + 1) + "] " + languages[i]);
                }

                source_choice = scanner.nextInt();
                scanner.nextLine();

                if (source_choice >= 1 && source_choice <= 8) {
                    break;
                }

                System.out.println("다시 입력해주세요");
            }

            // 번역할 언어

            int target_choice;

            while (true) {

                System.out.println(" \n \n 번역할 언어를 선택하세요");

                for (int i = 0; i < languages.length - 1; i++) {
                    System.out.println("[" + (i + 1) + "] " + languages[i]);
                }

                target_choice = scanner.nextInt();
                scanner.nextLine();

                if (target_choice >= 1 && target_choice <= 7) {
                    break;
                }

                System.out.println("다시 입력해주세요");
            }

            // 문장 입력

            String text;

            while (true) {

                System.out.println(" \n \n 번역할 문장을 입력하세요: ");
                text = scanner.nextLine();

                if (!text.trim().isEmpty()) {
                    break;
                }

                System.out.println(" \n \n 문장을 입력해주세요");
            }

            // 언어 코드 매핑

            String source = lang_codes[source_choice - 1];
            String target = lang_codes[target_choice - 1];

            // 번역 실행 및 기록

            /*
             * Java에서는 Python의 GoogleTranslator를
             * 그대로 사용할 수 없습니다.
             *
             * 번역 API를 연결하면 이 부분에서
             * 실제 번역을 실행할 수 있습니다.
             */

            String translated = text;

            System.out.println(" \n \n 번역 결과:");
            System.out.println(translated);

            System.out.println(" \n \n 번역 전");
            System.out.println("글자 수 : " + text.length());
            System.out.println("단어 수 : " + text.trim().split("\\s+").length);

            System.out.println(" \n \n 번역 후");
            System.out.println("글자 수 : " + translated.length());
            System.out.println("단어 수 : " + translated.trim().split("\\s+").length);

            // 기록 저장

            history.add("원본 : " + text);
            history.add("결과 : " + translated);
            history.add("------------------------------");

            try {

                FileWriter writer = new FileWriter(history_file, true);

                writer.write("원본 : " + text + "\n");
                writer.write("결과 : " + translated + "\n");
                writer.write("------------------------------\n");

                writer.close();

            } catch (IOException e) {
                System.out.println("오류가 발생했습니다");
            }

            while (true) {

                System.out.println(" \n \n ");
                System.out.println("[1] 메인 메뉴");
                System.out.println("[2] 종료");

                String menu = scanner.nextLine();

                if (menu.equals("1")) {
                    break;
                }

                else if (menu.equals("2")) {
                    System.out.println("프로그램 종료");
                    scanner.close();
                    return;
                }

                else {
                    System.out.println("다시 입력해주세요");
                }
            }
        }

        scanner.close();
    }
}